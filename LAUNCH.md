# Moving to bibliotheca-psychonautica.org

The site currently runs on **bibliotheca.psychedelicscience.eu**. Everything
that needs an absolute URL — hreflang, Open Graph, the sitemap — points there,
because a stale domain is worse than none: search engines get told the real
version lives somewhere else, and WhatsApp and Facebook fetch a preview image
that isn't there.

At the time of writing the `.org` is still live with the **old 2012 site**, so
nothing here should point at it until it actually serves this one.

## On the day

**1. Point the domain at GitHub Pages.** Change the one line in `CNAME`:

```
www.bibliotheca-psychonautica.org
```

Add the DNS record at the registrar, and wait for the certificate to issue
(GitHub does this automatically; it can take up to an hour).

**2. Restamp every absolute URL:**

```bash
python3 tools/set-site-url.py https://www.bibliotheca-psychonautica.org
python3 tools/i18n/i18n.py build
```

The first command rewrites hreflang, `og:url`, `og:image` and `sitemap.xml`
across all German pages; the second propagates them to the English ones.
Run `python3 tools/set-site-url.py` with no argument any time to see which
domain is currently in use.

**3. Check it took:**

```bash
curl -s https://www.bibliotheca-psychonautica.org/ | grep -o '<meta property="og:[^>]*>'
curl -s -o /dev/null -w '%{http_code}\n' https://www.bibliotheca-psychonautica.org/assets/og-image.jpg
```

The second must return `200`, or link previews will show no image.

**4. Re-scrape the preview caches.** WhatsApp, Facebook and LinkedIn cache
Open Graph data for weeks. Force a refresh at
<https://developers.facebook.com/tools/debug/> — WhatsApp uses the same cache.

**5. Decide what happens to the old site** at the `.org`, and whether any of
its URLs need redirecting.

## Still open at launch

- Impressum and Datenschutz are both marked *Vorläufige Fassung* and are now
  published in two languages. They need a lawyer, and a line stating which
  language version is binding.
- `Beitrag.html` is still placeholder text and is marked `noindex`. Either
  give it real content or remove it and the links pointing at it.
- The unverified quotation attributed to Prof. Torsten Passie on the homepage
  needs written permission or removal.
- Both forms open a mail draft rather than submitting. If the visitor has no
  mail client configured, nothing happens and you never learn the enquiry was
  attempted.
