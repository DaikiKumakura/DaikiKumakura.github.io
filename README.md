# Daiki Kumakura — portfolio

Published at https://daikikumakura.github.io/ in Japanese and English.

Edit `_portfolio/content/site.json` and Markdown under `_portfolio/content/articles/`. Both languages share templates and metadata. Articles may be written in one language; drafts are excluded from the public build.

## Update

Python 3.11 or newer:

```sh
python -m pip install -r _portfolio/requirements.txt
cd _portfolio
python -m unittest -q
python stage_publication.py
cd ..
git diff
```

Review, commit and push the source and generated files together. Existing GitHub Pages branch publishing serves the root of `main`; `_config.yml` excludes the maintenance source directory. No dependency installation is required on each page view. Do not edit generated `ja/` or `en/` HTML directly.

`python build.py --preview` writes a local preview to `_portfolio/dist` with sample drafts and noindex. Never copy that preview to the repository root. `stage_publication.py` always performs a production build with strict translation checking and only removes obsolete files listed in its own previous publication manifest. It never pushes.

## Existing URLs

- `publication.html` → `en/publications.html`
- `publication_jpn.html` → `ja/publications.html`
- `cv.html`, `research.html` → `ja/about.html`
- `education.html` → `ja/activities.html#teaching`
- `gallery.html` → `ja/writing.html`
- `link.html` → `article/article_00.html`

These static redirect pages use meta refresh with a visible fallback link and canonical URL (not an HTTP 301). The existing article, PDFs, notebook, verification file and other assets retain their paths. Historical versions remain in Git history.

## Rollback

The pre-migration commit is `2a7c47d3c842bc4b0071f19640d0bc1989d3ccc8`. Revert the migration commit in a new commit and push; do not rewrite shared history. Verify the Pages deployment and live URLs after any publication or rollback.
