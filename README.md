# Daiki Kumakura — portfolio

[Website](https://daikikumakura.github.io/) · One English site. Articles may be in English or Japanese; translations are optional.

## Where to edit

```text
site/
  content/site.json    Profile, software, publications and activities
  content/articles/   Your Markdown articles (created when needed)
  assets/             Shared CSS, favicon and licensed SVG illustrations
  templates/          Shared page layouts
  static/             Legacy resources and Google verification file
  fixtures/           Article samples used only by tests
  build.py, seo.py     Static-site generator and search metadata
  test_*.py           Build, link and metadata checks
.github/workflows/    Test, build and deploy to GitHub Pages
```

Edit `site/content/site.json` for existing records. Push to `main`; GitHub Actions tests the source and deploys the generated site. **Do not maintain or commit generated HTML.** Build output is ignored at `site/dist/`. Pages settings use **GitHub Actions**, not branch publishing.

Navigation: Home, Profile, Writing, Software, Publication, Activity. Home contains only the introduction. `/`, `/index.html` and `/home.html` display the same content, with `/` as the canonical URL.

## Add an article

```sh
python -m pip install -r site/requirements.txt
python site/build.py new article-slug --lang en --title "Article title"
```

Use `--lang ja` for Japanese. Edit the generated Markdown and `meta.json` in `site/content/articles/article-slug/`. Set `draft` to `false` when ready. Categories are `tutorial`, `note`, `essay` (blog), and `paper` (not peer reviewed). The URL is `/writing/article-slug.html`. Working papers also appear under Publication.

An original in one language is enough. Optional translations share code and figures in `shared/`; after reviewing one, run `python site/build.py review-translation article-slug --lang en` (or `ja`). Tests use their own fixtures, never your draft directory.

## Preview and check

Python 3.11 or newer:

```sh
python -m pip install -r site/requirements.txt
python -m unittest discover -s site -q
python site/build.py --strict-translations
python -m http.server 8000 --directory site/dist
```

Open `http://localhost:8000/`. To include drafts locally, use `python site/build.py --preview`; preview pages are marked noindex. Production deployment always rebuilds without drafts. No build tools run in the visitor's browser.

## Preserved URLs

- `ja/` and `en/` section pages → corresponding English pages
- `about.html`, `cv.html`, `research.html` → `profile.html`
- `publications.html`, `publication_jpn.html` → `publication.html`
- `activities.html` → `activity.html`
- `education.html` → `activity.html#teaching`
- `gallery.html` → `writing.html`
- `link.html` → `article/article_00.html`

Redirects use meta refresh, a visible fallback link and canonical metadata; they are not HTTP 301 responses. Files in `site/static/` are published at their original paths, including `/article/article_00.html` and `/etc_files/`. Older unused templates remain available in Git history.

The sitemap contains canonical content pages only. Keep the Bing verification tag in `site/templates/base.html` and the Google file in `site/static/`. Structured identity/publication metadata comes from the same source as visible content. Search rankings and AI citations are not guaranteed.

## Third-party artwork

The favicon and page illustrations are downloaded, self-hosted assets with commercial-use permissions. Their exact sources, file mapping, and license terms are recorded in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). Keep that file with the assets when replacing or redistributing them.

## Restore an earlier version

Revert the relevant commit and let Actions rebuild. Do not rewrite shared history. The source-only migration follows commit `c100985bb567f79c161826ae3a29341ad5d08d8e`; returning to that older branch-published version also requires restoring the Pages source setting. Verify the deployment and live URLs after a rollback.

