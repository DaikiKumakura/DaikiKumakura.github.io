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

An original in one language is enough. A Japanese original may add `"english": {"title": ..., "summary": ...}` to `meta.json`; it is shown as a short English summary on the article and on the Profile page, and used in search metadata. List articles on the Profile page under `analysis_topics` in `site.json`; unpublished or scheduled articles appear only once they are live. Optional translations share code and figures in `shared/`; after reviewing one, run `python site/build.py review-translation article-slug --lang en` (or `ja`). Tests use their own fixtures, never your draft directory.

## Scheduled articles

Set `publish_at` in `meta.json` to a timezone-aware timestamp, for example `2026-10-04T09:00:00+09:00`, and set `date` to its local calendar date. Set `draft` to `false` only after review. Production builds omit the article, its shared files, and sitemap entry until that time. Preview builds include it and remain noindex.

GitHub Actions rebuilds daily at 00:00 UTC (09:00 JST). Scheduled runs can be delayed or skipped by GitHub; this is not an exact-time publishing guarantee. Use the existing manual workflow dispatch if a scheduled run is missed. Source files in this public repository are visible before the website publication time; scheduling does not make them confidential.

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

Old URLs that still appear in search results redirect to the current pages (`LEGACY_REDIRECTS` in `site/build.py`):

- `ja/` and `en/` section pages → corresponding English pages
- `about.html`, `cv.html`, `research.html` → `profile.html`
- `publications.html`, `publication_jpn.html` → `publication.html`
- `activities.html` → `activity.html`, `education.html` → `activity.html#teaching`
- `gallery.html`, `link.html`, `japanese.html` → `writing.html` or the home page

GitHub Pages cannot send HTTP 301, so each redirect is an instant meta refresh with a canonical link and a visible fallback link. Redirect pages are not in the sitemap. `/article/article_00.html` stays retired.

The sitemap contains canonical content pages only. Keep the Bing verification tag in `site/templates/base.html` and the Google file in `site/static/`. Structured identity/publication metadata comes from the same source as visible content. Search rankings and AI citations are not guaranteed.

## Third-party artwork

The favicon and page illustrations are downloaded, self-hosted assets with commercial-use permissions. Their exact sources, file mapping, and license terms are recorded in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). Keep that file with the assets when replacing or redistributing them.

## Restore an earlier version

Revert the relevant commit and let Actions rebuild. Do not rewrite shared history. The source-only migration follows commit `c100985bb567f79c161826ae3a29341ad5d08d8e`; returning to that older branch-published version also requires restoring the Pages source setting. Verify the deployment and live URLs after a rollback.
