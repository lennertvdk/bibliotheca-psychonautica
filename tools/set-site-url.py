#!/usr/bin/env python3
"""Point every absolute URL on the site at the domain that actually serves it.

hreflang, canonical Open Graph URLs and the sitemap all have to be fully
qualified, so they hard-code a domain. That domain changes when the site
moves, and a stale one is worse than none: search engines are told the real
version lives somewhere else, and WhatsApp, Signal and Facebook fetch a
preview image that isn't there.

    python3 tools/set-site-url.py                     # show the current domain
    python3 tools/set-site-url.py https://example.org # switch to a new one

Then rebuild the English pages:

    python3 tools/i18n/i18n.py build
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERN = re.compile(r'https://[a-z0-9.-]+(?=/(?:index\.html|en/|assets/|Der-Verein|Themen-und-'
                     r'Sammlungen|Neuigkeiten|Beitrag|Kontakt|Mitglied-werden|Spenden|'
                     r'Impressum|Datenschutz))')


def targets():
    pages = [p for p in glob.glob(os.path.join(ROOT, "*.html"))]
    return pages + [os.path.join(ROOT, "sitemap.xml")]


def current():
    found = set()
    for path in targets():
        if os.path.exists(path):
            found |= set(PATTERN.findall(open(path, encoding="utf-8").read()))
    return found


def main():
    if len(sys.argv) < 2:
        found = current()
        if not found:
            print("No absolute site URLs found.")
        for url in sorted(found):
            print(url)
        print("\nPass a new URL to change it, e.g.")
        print("  python3 tools/set-site-url.py https://www.bibliotheca-psychonautica.org")
        return

    new = sys.argv[1].rstrip("/")
    if not new.startswith("https://"):
        sys.exit("The URL must start with https:// — crawlers require a fully qualified URL.")

    changed = 0
    for path in targets():
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        swapped = PATTERN.sub(new, text)
        if swapped != text:
            open(path, "w", encoding="utf-8").write(swapped)
            print("  updated", os.path.relpath(path, ROOT))
            changed += 1

    print(f"\n{changed} file(s) now point at {new}")
    print("Now run: python3 tools/i18n/i18n.py build")


if __name__ == "__main__":
    main()
