# English site generator

The German pages in the repo root are the source of truth. Every page under
`en/` is generated from its German counterpart with the text swapped out, so
markup, inline styles, layout and images stay identical by construction.

## The one rule

**Never edit anything in `en/` by hand.** The next build overwrites it.
English wording lives in `strings.de-en.json`.

## Everyday workflow

Edit the German page as usual, then:

```
python3 tools/i18n/i18n.py build
```

If you added or changed German text, the build stops and tells you exactly
which sentences have no English yet:

```
1 German string(s) have no translation in tools/i18n/strings.de-en.json:

  "Die Bibliothek zieht um."
      in Neuigkeiten.html

Add them to the file above, then run this again.
```

Add the pair to `strings.de-en.json` and run it again. That failure is the
point of the tool: a new German sentence cannot silently reach the English
site untranslated.

`python3 tools/i18n/i18n.py check` reports the same thing without writing
files — useful before committing.

## What the build handles for you

- translates text and the attributes a reader sees (`alt`, `title`,
  `placeholder`, `aria-label`, `meta description`)
- rewrites internal links to the English filenames
- rewrites `assets/...` paths to `../assets/...`
- switches `lang="de"` to `lang="en"`
- turns the header's `EN` toggle into a `DE` toggle pointing back at the
  German page
- translates text that is not markup: the contact form's mailto subject and
  body, the IBAN copy-button feedback, the checkbox `value`s, and the
  `?interesse=` deep link whose token has to match a checkbox value

Because English is rebuilt from the German *markup*, a layout or styling
change needs no translation work at all — just rerun the build.

## Adding a page

Add it to `PAGES` in `i18n.py`:

```python
PAGES = {
    ...
    "Neue-Seite.html": "new-page.html",
}
```

Then run the build; it will list the new page's German text as untranslated.

## Things worth knowing

- The legal entity name *Verein Bibliotheca Psychonautica* is deliberately
  left untranslated.
- `Impressum.html` / `Datenschutz.html` are marked "Vorläufige Fassung" and
  are still under legal review. When the German is finalised, treat the
  English as a convenience translation and say which version is binding.
- Strings inside `<script>` are matched as literal source text in `JS_MAP`,
  so changing the surrounding JavaScript quoting will silently stop them
  matching. `check` will not catch that — grep for the German if you touch
  the scripts.
- If the English site ever needs to *diverge* from the German (an
  English-only page, or different wording for an international audience),
  that page has to come out of `PAGES` and be maintained by hand.
