# Bibliotheca Psychonautica

Static website export based on the Claude Design handoff for Bibliotheca Psychonautica.

## Publish on GitHub Pages

The ready-to-publish website is available at the repository root, with the generated source export also kept in [`site/`](site/). The root contains the designed homepage as `index.html`, all linked pages, and local image assets.

1. Create or open the `bibliotheca-psychonautica` GitHub repository.
2. Copy or push this project to the repository.
3. In GitHub, open **Settings → Pages**.
4. Choose **Deploy from a branch**, select the publishing branch, and set the folder to `/ (root)`.

GitHub Pages will serve [`index.html`](index.html) as the homepage.

## Rebuild the export

The original Claude Design files remain in both handoff folders. The lowercase folder is the canonical build source. If those files change, regenerate the publishable site with:

```sh
node build-site.js
```

The exporter inlines the shared header and footer, removes Claude preview-only markup, rewrites `.dc.html` links to normal `.html` links, and copies the supplied assets.
