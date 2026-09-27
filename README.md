# Daiki Kumakura — portfolio

Published at https://daikikumakura.github.io/. One English site; articles can be written in English or Japanese without requiring a translation.

Edit `_portfolio/content/site.json` once for profile, software, publication and activity records. Values are plain English strings. Articles live under `_portfolio/content/articles/`; drafts are excluded from publication.

Navigation: Home, Profile, Writing, Software, Publication, Activity. The corresponding files are `home.html`, `profile.html`, `writing.html`, `software.html`, `publication.html`, `activity.html`. The root and `index.html` show exactly the same Home content; their canonical URL is the root.

## Add an article

```sh
cd _portfolio
python build.py new article-slug --lang en --title "Article title"
```

Use `--lang ja` for a Japanese article. Edit the generated Markdown and `meta.json`, then change `draft` to `false` when ready. Categories: `tutorial`, `note`, `essay` (blog), `paper` (not peer reviewed). One original is enough; the public URL is `writing/article-slug.html`. Add a second locale only if you want a translation. Shared code/figures stay in `shared/`; review an optional translation with `python build.py review-translation article-slug --lang en` (or `ja`).

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

Review, commit and push the source and generated files together. Existing GitHub Pages branch publishing serves the root of `main`; `_config.yml` excludes the maintenance source directory. No dependency installation is required on each page view. Do not edit generated HTML directly. Favicon and the original decorative isometric illustration are lightweight SVGs under `_portfolio/assets/`.

`python build.py --preview` writes a local preview to `_portfolio/dist` with sample drafts and noindex. Never copy that preview to the repository root. `stage_publication.py` always performs a production build with strict translation checking and only removes obsolete files listed in its own previous publication manifest. It never pushes.

## Existing URLs

- `ja/` and `en/` section pages → corresponding root-level English pages
- `about.html`, `cv.html`, `research.html` → `profile.html`
- `publications.html`, `publication_jpn.html` → `publication.html`
- `activities.html` → `activity.html`
- `education.html` → `activity.html#teaching`
- `gallery.html` → `writing.html`
- `link.html` → `article/article_00.html`

These static redirect pages use meta refresh with a visible fallback link and canonical URL (not an HTTP 301). The existing article, PDFs, notebook, verification file and other assets retain their paths. Historical versions remain in Git history.

The sitemap lists canonical content pages only. `robots.txt` allows crawling, including search-engine and AI-search crawlers. Profile identity links and publication metadata are generated from the same source as visible text. This does not guarantee rankings or AI citations. Keep the Bing verification meta tag in the shared base template.

## Rollback

The pre-migration commit is `2a7c47d3c842bc4b0071f19640d0bc1989d3ccc8`. Revert the migration commit in a new commit and push; do not rewrite shared history. Verify the Pages deployment and live URLs after any publication or rollback.
