# Daiki Kumakura — portfolio

[Website](https://daikikumakura.github.io/) · One English site. Articles may be in English or Japanese; translations are optional.

## Where to edit

```text
site/
  content/site.json    Profile, software, publications and activities
  content/articles/   Your Markdown articles (created when needed)
  assets/             Shared CSS and favicon
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

## Search results and social previews

- **Search-result text.** A locale in `meta.json` may add `seo_title` (up to about 60 half-width cells; Japanese characters count twice, and no site name is appended) and `seo_description` (up to about 160 characters). They change only the page `<title>`, the meta and Open Graph text; the heading and the structured-data headline keep the full title. Editing them does not unreview a translation. Every build prints `seo_warnings` for titles or descriptions that search engines would cut, and for articles without a card. The warnings are advisory.
- **Social card.** `site/content/articles/<slug>/og.png` (1200×630) is published as `writing/og/<slug>.png` together with its article, never earlier, and is used for `og:image`. Without it the first figure is used, which LinkedIn may crop. Make cards with `python site/make_og_cards.py <slug>` or `--live` (needs Pillow; an SVG figure is rendered with Microsoft Edge). Pages without an article use `assets/og-default.png` (`--default`).
- **Software pages.** A `software` entry in `site.json` that has `slug`, `headline` and a 60–160 character `summary` gets `software/<slug>.html` (description, installation, status, links and optional `related_articles`, which appear only once live). The Software list links to it, and the sitemap and `llms.txt` list it.
- **Tools, glossary and catalogs.** A folder `site/content/reference/<slug>/` with `meta.json`, `en.md` and `ja.md` (both languages are required) becomes `tools/`, `glossary/` or `catalog/<slug>.html` (English) and `<slug>-ja.html`, depending on `kind` (`tool`, `term`, `catalog`). Each locale needs `title`, `summary`, `seo_title` and `seo_description`; `faq` (question and answer pairs) becomes an FAQ section and `FAQPage` data; `related_articles` appear only once live. All of them are listed on `reference.html`, the sitemap and `llms.txt`. The anti-PD-1 exposure explorer (`tools/anti-pd1-exposure.html`) only looks up numbers computed by the article's analysis: `python site/make_tool_data.py` regenerates `site/assets/tools/anti-pd1-exposure-data.json` from the article's companion zip, and `site/test_tool_data.py` checks it against the article's table.
- **Writing index in two languages.** `writing.html` lists every article with its English title and summary and `writing-ja.html` lists them in Japanese, so no list mixes the two. Each entry links to the other language, an article without an English version appears with an "in Japanese" note (and its English summary), and the two pages are tied by `hreflang`, `x-default`, the sitemap and `llms.txt`. The home page's recent writing is English.
- **Citation tags and glossary links.** Every article carries `citation_*` and Dublin Core `DC.*` meta tags (title, author, date, language, DOIs of the cited works) that reference managers and Google Scholar read, and lists the glossary pages that name it in `related_articles` (also as `mentions` in its structured data).
- **Image sitemap and the About page.** The sitemap lists each article's figures (`<image:image>`) so that they can appear in image search. `content/reference/about-these-analyses/` (kind `policy`, published as `about/`) states the scope, sources, checks and correction practice and is linked from every page's footer and from `reference.html`.
- **Feeds.** `feed.xml` keeps each article in its original language (unchanged, as registered with the search engines). `feed-en.xml` and `feed-ja.xml` carry titles and summaries in one language each and link to that language's page; an article without a version in that language stays in the feed in its original language. All three are advertised in every page's `<head>` and in `robots.txt`.
- **Hidden articles.** Rescheduling a published article makes its URL return 404 until it is live again. The workflow warns about this (`site/check_dropped_urls.py`); it does not block the deploy.

## Scheduled articles

Set `publish_at` in `meta.json` to a timezone-aware timestamp, for example `2026-10-04T09:00:00+09:00`, and set `date` to its local calendar date. Set `draft` to `false` only after review. Production builds omit the article, its shared files, and sitemap entry until that time. Preview builds include it and remain noindex.

GitHub-hosted Actions rebuilds at 09:07 and 09:37 JST, with an hourly catch-up at minute 17. Source, figures and downloads must already be pushed to `main`; no local computer, browser or Codex session needs to remain running. Every successful build includes all eligible articles, so a missed run is recovered by the next successful run. After deployment, a separate job checks the live article URLs and sitemap against the exact uploaded artifact, retrying for CDN propagation; failures are visible in Actions. IndexNow notification follows that check.

GitHub can delay or drop scheduled runs; neither exact-time publication nor availability during a GitHub outage is guaranteed. Manual workflow dispatch remains available. Public repositories with 60 days of no repository activity can have scheduled workflows disabled by GitHub; check/re-enable Actions before a new long-term schedule. Source files in this public repository are visible before the website publication time; scheduling does not make them confidential.

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

The favicon is a downloaded, self-hosted asset with a permissive license. Its exact source and license terms are recorded in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). Keep that file with the asset when replacing or redistributing it.

## Restore an earlier version

Revert the relevant commit and let Actions rebuild. Do not rewrite shared history. The source-only migration follows commit `c100985bb567f79c161826ae3a29341ad5d08d8e`; returning to that older branch-published version also requires restoring the Pages source setting. Verify the deployment and live URLs after a rollback.
