#!/usr/bin/env python3
"""Generate the English pages under en/ from the German originals.

German is the single source of truth. Every English page is its German
counterpart with the text swapped out, so markup, inline styles, layout and
assets stay identical by construction.

    python3 tools/i18n/i18n.py check    # list German text with no translation
    python3 tools/i18n/i18n.py build    # regenerate every page in en/

`build` refuses to run while anything is untranslated, so a new German
sentence can never slip into the English site in German.
"""

import json
import os
import re
import sys
from html import escape
from html.parser import HTMLParser
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STRINGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "strings.de-en.json")
OUTDIR = "en"

# German page -> English filename under en/. Add new pages here.
PAGES = {
    "index.html": "index.html",
    "Der-Verein.html": "about.html",
    "Themen-und-Sammlungen.html": "collections.html",
    "Neuigkeiten.html": "news.html",
    "Beitrag.html": "article.html",
    "Kontakt.html": "contact.html",
    "Mitglied-werden.html": "join.html",
    "Spenden.html": "donate.html",
    "Impressum.html": "imprint.html",
    "Datenschutz.html": "privacy.html",
    # internal handover pages, not in the public navigation
    "Uebersicht.html": "overview.html",
    "Designsystem.html": "design-system.html",
    "Mobile-Ansichten.html": "mobile-views.html",
    "Wortmarke.html": "wordmark.html",
}

# Text that is not markup and so is invisible to the HTML parser below.
# Checkbox values double as the ?interesse= deep-link token, so both sides
# of that link are rewritten together.
VALUE_MAP = {
    "Bücher und Sammlungen": "Books and collections",
    "Nachlässe": "Estates",
    "Archivierung und Digitalisierung": "Archiving and digitisation",
    "Projektaufbau": "Project development",
}

# User-facing strings inside <script> blocks, matched as literal source text.
JS_MAP = {
    "'Mitarbeit: '": "'Getting involved: '",
    "'Anfrage zur Mitarbeit'": "'Enquiry about getting involved'",
    "'E-Mail: '": "'Email: '",
    "'Interessen: '": "'Interests: '",
    "'noch offen'": "'not yet decided'",
    "'IBAN kopiert'": "'IBAN copied'",
    "'Kopieren fehlgeschlagen'": "'Copy failed'",
    "'Mitgliedschaft: '": "'Membership: '",
    "'Anmeldung Mitgliedschaft'": "'Membership application'",
    "'noch nicht gewählt'": "'not yet chosen'",
    "'Vorname: '": "'First name: '",
    "'Name: '": "'Surname: '",
    "'Ort: '": "'Town/city: '",
    "'Land: '": "'Country: '",
    "'Firma: '": "'Company: '",
    "'Strasse: '": "'Street: '",
    "'Telefon: '": "'Phone: '",
    "'Webseite: '": "'Website: '",
}

SKIP_TAGS = {"style", "script"}
TEXT_ATTRS = {"alt", "title", "placeholder", "aria-label", "content", "value", "data-tier"}
HAS_LETTER = re.compile(r"[A-Za-zÄÖÜäöüß]")


def translatable_attr(name, value, attrs):
    """Whether this attribute holds prose a reader will see."""
    if name not in TEXT_ATTRS or not value:
        return False
    if name == "content":
        prop = attrs.get("property", "")
        if prop in ("og:title", "og:description"):
            return True
        if attrs.get("name") not in ("description", "keywords"):
            return False
    if name == "value" and attrs.get("type") not in ("submit", "button", None):
        return False
    return bool(HAS_LETTER.search(value))


class Walker(HTMLParser):
    """Visits every piece of reader-facing text in a page."""

    def __init__(self, src, on_text, on_attr):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.on_text = on_text
        self.on_attr = on_attr
        self.stack = []
        self.line_start = [0]
        for line in src.splitlines(keepends=True):
            self.line_start.append(self.line_start[-1] + len(line))

    def abs_offset(self):
        line, col = self.getpos()
        return self.line_start[line - 1] + col

    def tag_span(self, start):
        """Offset just past the '>' that closes the tag starting at `start`."""
        i, quote_char = start, None
        while i < len(self.src):
            ch = self.src[i]
            if quote_char:
                if ch == quote_char:
                    quote_char = None
            elif ch in "\"'":
                quote_char = ch
            elif ch == ">":
                return i + 1
            i += 1
        return len(self.src)

    def _tag(self, tag, attrs):
        start = self.abs_offset()
        raw = self.src[start:self.tag_span(start)]
        as_dict = dict(attrs)
        for name, value in attrs:
            if value:
                self.on_attr(name, value, as_dict, start, raw)

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        self._tag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self._tag(tag, attrs)

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass

    def handle_data(self, data):
        if any(t in SKIP_TAGS for t in self.stack):
            return
        core = data.strip()
        if core and HAS_LETTER.search(core):
            self.on_text(core, data, self.abs_offset())


def rewrite_link(value, source_page):
    """Point a German page's link at its English counterpart."""
    if value.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
        return value
    if value.startswith("en/"):
        # the DE->EN toggle becomes the EN->DE toggle
        return "../" + source_page
    if value.startswith("assets/"):
        return "../" + value
    base, rest = re.match(r"([^?#]*)(.*)$", value).groups()
    if base in PAGES:
        for de_value, en_value in VALUE_MAP.items():
            rest = rest.replace(quote(de_value), quote(en_value)).replace(de_value, en_value)
        return PAGES[base] + rest
    return value


def translate_page(source_page, translations, missing):
    src = open(os.path.join(ROOT, source_page), encoding="utf-8").read()
    edits = []

    def on_text(core, data, start):
        if core not in translations:
            missing.setdefault(core, set()).add(source_page)
            return
        edits.append((start, start + len(data), data.replace(core, translations[core], 1)))

    def on_attr(name, value, attrs, start, raw):
        new = None
        prop = attrs.get("property", "")
        if name == "content" and prop == "og:url":
            new = value.replace("/" + source_page, "/en/" + PAGES[source_page])
        elif name == "content" and prop == "og:locale":
            new = "en_GB"
        if new is None and translatable_attr(name, value, attrs):
            core = value.strip()
            if core in translations:
                new = value.replace(core, translations[core], 1)
            else:
                missing.setdefault(core, set()).add(source_page)
        if new is None and name in ("href", "src"):
            new = rewrite_link(value, source_page)
        if new is None or new == value:
            return
        # the parser hands back decoded attribute values, but `raw` still holds
        # the entities, so try both spellings and answer in the same one
        for source_form, target in ((value, new), (escape(value), escape(new))):
            m = re.search(re.escape(name) + r'(\s*=\s*)(["\'])' + re.escape(source_form) + r"\2", raw)
            if m:
                q = m.group(2)
                edits.append((start + m.start(), start + m.end(), f"{name}={q}{target}{q}"))
                break

    Walker(src, on_text, on_attr).feed(src)

    out = src
    for start, end, replacement in sorted(edits, key=lambda e: -e[0]):
        out = out[:start] + replacement + out[end:]
    # `lang="de"` only as a whole attribute - the lookbehind keeps this from
    # matching inside `hreflang="de"`, which must stay German on both sides.
    out = re.sub(r'(?<![\w-])lang="de"', 'lang="en"', out)
    for de_value, en_value in VALUE_MAP.items():
        out = out.replace(f'name="interesse" value="{de_value}"', f'name="interesse" value="{en_value}"')
    for de_js, en_js in JS_MAP.items():
        out = out.replace(de_js, en_js)
    return out


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else "build"
    if command not in ("build", "check"):
        sys.exit(__doc__)

    translations = json.load(open(STRINGS, encoding="utf-8"))
    missing, pages = {}, {}
    for source_page, target in PAGES.items():
        pages[target] = translate_page(source_page, translations, missing)

    if missing:
        print(f"{len(missing)} German string(s) have no translation in")
        print(f"{os.path.relpath(STRINGS, ROOT)}:\n")
        for text in sorted(missing):
            where = ", ".join(sorted(missing[text]))
            print(f'  "{text}"\n      in {where}\n')
        print("Add them to the file above, then run this again.")
        sys.exit(1)

    if command == "check":
        print(f"All German text in {len(PAGES)} pages is translated.")
        return

    written = 0
    os.makedirs(os.path.join(ROOT, OUTDIR), exist_ok=True)
    for target, html in pages.items():
        path = os.path.join(ROOT, OUTDIR, target)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if old != html:
            open(path, "w", encoding="utf-8").write(html)
            print(f"  updated {OUTDIR}/{target}")
            written += 1
    print(f"\n{len(PAGES)} pages generated, {written} changed.")


if __name__ == "__main__":
    main()
