"""Build a small, bilingual static site. Python 3.11+; no server runtime."""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import sys
from datetime import date
from urllib.parse import urljoin

SITE_URL = 'https://daikikumakura.github.io/'
LEGACY_REDIRECTS = {'publication.html':'en/publications.html', 'publication_jpn.html':'ja/publications.html', 'cv.html':'ja/about.html', 'research.html':'ja/about.html', 'education.html':'ja/activities.html#teaching', 'gallery.html':'ja/writing.html', 'link.html':'article/article_00.html'}

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / '.deps'))
import markdown
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

LANGS = ('ja', 'en')
CATEGORIES = ('tutorial', 'note', 'paper', 'essay')
UI = {
    'ja': dict(nav=dict(index='ホーム', about='プロフィール', publications='研究業績', software='ソフトウェア', writing='記事', activities='活動'), skip='本文へ', preview='試作・プレビュー。本番サイトではありません。', unavailable='未翻訳', navigation='ページ', selected='主な論文', expertise='専門', background='経歴', empty='公開記事はまだありません。', draft='下書き', draft_notice='下書き・見本。公開記事ではありません。', unreviewed='未査読', working_papers='未査読の論考', stale='原文または共通資料が更新されています。この翻訳は再確認が必要です。', toc='目次', back='記事一覧へ', partial='この試作は代表データのみです。全業績の移行は未実施です。', categories=dict(tutorial='チュートリアル', note='技術メモ', paper='未査読の論考', essay='ブログ')),
    'en': dict(nav=dict(index='Home', about='About', publications='Publications', software='Software', writing='Writing', activities='Activities'), skip='Skip to content', preview='Prototype preview. This is not the live website.', unavailable='not translated', navigation='Pages', selected='Selected publications', expertise='Expertise', background='Background', empty='No published articles yet.', draft='Draft', draft_notice='Draft sample, not a published article.', unreviewed='Not peer reviewed', working_papers='Working papers', stale='The original or shared resources have changed. This translation needs review.', toc='On this page', back='All articles', partial='This prototype contains selected records only. The full bibliography has not been migrated.', categories=dict(tutorial='Tutorial', note='Technical note', paper='Working paper', essay='Blog')),
}
UI['ja'].update(background='職歴・研究歴', education='学歴', thesis='博士論文', awards='受賞')
UI['en'].update(background='Appointments', education='Education', thesis='Doctoral thesis', awards='Awards')
UI['ja'].update(publication_types=dict(journal='学術誌論文', proceedings='会議録・書籍章', review='総説・解説', preprint='プレプリント（未査読）', thesis='学位論文'), activity_types=dict(presentations='学会・セミナー発表', service='開催・運営・協力', outreach='一般向け活動・取材', teaching='教育'), sources='関連資料', online='オンライン公開', activity_note='既存サイトの記録と公開資料に基づく一覧です。共著発表には、自身が発表者ではない記録も含みます。', records='件')
UI['en'].update(publication_types=dict(journal='Journal articles', proceedings='Proceedings and book chapters', review='Reviews and commentary', preprint='Preprints (not peer reviewed)', thesis='Theses'), activity_types=dict(presentations='Conference and seminar presentations', service='Organization and service', outreach='Outreach and media', teaching='Teaching'), sources='Resources', online='Published online', activity_note='Compiled from the previous website and public records. Co-authored presentations include work presented by other authors.', records='records')

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def safe_relative(name):
    p = Path(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name:
        raise ValueError(f'Unsafe relative path: {name}')
    return p

def bilingual(value, label):
    if not isinstance(value, dict) or any(not value.get(k) for k in LANGS):
        raise ValueError(f'Missing ja/en value: {label}')

def validate_site(site):
    for key in ('profile', 'expertise', 'display_name'):
        bilingual(site[key], key)
    for row in site['career']:
        bilingual(row, 'career')
    for collection in ('education', 'awards'):
        for row in site[collection]:
            bilingual(row, collection)
    bilingual(site['thesis']['title'], 'thesis')
    for row in site['research_background']:
        bilingual(row['title'], 'research title')
        bilingual(row['body'], 'research body')
    for row in site['software']:
        for key in ('status', 'description', 'note'):
            bilingual(row[key], key)
        if not isinstance(row.get('featured'), bool):
            raise ValueError('Software featured must be true or false')
        for link in row['links']:
            bilingual(link['label'], 'software link')
    for row in site['activities']:
        for key in ('role', 'title'):
            bilingual(row[key], key)
    for row in site['activities']:
        if row['category'] not in UI['en']['activity_types']:
            raise ValueError('Unknown activity category')
    for row in site['publications']:
        if row['kind'] not in UI['en']['publication_types']:
            raise ValueError('Unknown publication kind')
    for collection in ('software', 'publications', 'activities'):
        ids = [p['id'] for p in site[collection]]
        if len(ids) != len(set(ids)):
            raise ValueError(f'Duplicate ID: {collection}')

def fingerprint(folder, meta):
    """Original title, summary, body, and all shared assets form one revision."""
    source = meta['source_language']
    digest = hashlib.sha256()
    digest.update(json.dumps(meta['locales'][source], sort_keys=True, ensure_ascii=False).encode())
    digest.update((folder / f'{source}.md').read_bytes())
    for path in sorted((folder / 'shared').rglob('*')):
        if path.is_file():
            digest.update(path.relative_to(folder).as_posix().encode())
            digest.update(path.read_bytes())
    return digest.hexdigest()

def load_articles(content, preview=False):
    entries = []
    for folder in sorted((content / 'articles').glob('*')):
        if not folder.is_dir():
            continue
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', folder.name):
            raise ValueError(f'Invalid article slug: {folder.name}')
        meta = read_json(folder / 'meta.json')
        if meta['source_language'] not in LANGS or meta['category'] not in CATEGORIES:
            raise ValueError(f'Invalid language/category: {folder.name}')
        if not isinstance(meta.get('draft'), bool):
            raise ValueError(f'draft must be true or false: {folder.name}')
        date.fromisoformat(meta['date'])
        if meta['source_language'] not in meta['locales']:
            raise ValueError('Original language is missing')
        for lang, data in meta['locales'].items():
            if lang not in LANGS or not data.get('title') or not data.get('summary'):
                raise ValueError(f'Invalid article locale: {folder.name}/{lang}')
            if not (folder / f'{lang}.md').is_file():
                raise ValueError(f'Missing article body: {folder.name}/{lang}.md')
        for path in folder.rglob('*'):
            if path.is_symlink():
                raise ValueError('Symlinks are not supported in article content')
        if meta['draft'] and not preview:
            continue
        revision = fingerprint(folder, meta)
        stale = {lang: lang != meta['source_language'] and meta.get('reviewed', {}).get(lang) != revision for lang in meta['locales']}
        entries.append(dict(meta=meta, folder=folder, slug=folder.name, stale=stale))
    return sorted(entries, key=lambda a: (a['meta']['date'], a['slug']), reverse=True)

def render_body(article, lang):
    body = (article['folder'] / f'{lang}.md').read_text(encoding='utf-8')
    # One shared source file can be included by both translations without duplication.
    def include(match):
        language, filename = match.groups()
        relative = safe_relative(filename)
        shared = (article['folder'] / 'shared').resolve()
        path = (shared / relative).resolve()
        if not path.is_relative_to(shared) or not path.is_file():
            raise ValueError(f'Missing shared code: {filename}')
        return '\n<pre><code class="language-' + html.escape(language) + '">' + html.escape(path.read_text(encoding='utf-8')) + '</code></pre>\n'
    body = re.sub(r'^\{\{code:([a-zA-Z0-9_-]+):([^}\n]+)\}\}\s*$', include, body, flags=re.M)
    parser = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'attr_list'])
    return parser.convert(body), parser.toc

def build(project=BASE, preview=False, strict_translations=False):
    project = Path(project)
    site = read_json(project / 'content/site.json')
    validate_site(site)
    entries = load_articles(project / 'content', preview)
    warnings = [f"Translation needs review: {a['slug']}/{lang}" for a in entries for lang, stale in a['stale'].items() if stale]
    if warnings and strict_translations:
        raise ValueError('\n'.join(warnings))
    env = Environment(loader=FileSystemLoader(project / 'templates'), autoescape=select_autoescape(['html']), undefined=StrictUndefined)
    outputs = {}
    for asset in (project / 'assets').rglob('*'):
        if asset.is_file():
            outputs['assets/' + asset.relative_to(project / 'assets').as_posix()] = asset.read_bytes()
    for lang in LANGS:
        listings = []
        for a in entries:
            m = a['meta']
            actual = lang if lang in m['locales'] else m['source_language']
            labels = ' / '.join('日本語' if k == 'ja' else 'English' for k in m['locales'])
            listings.append(dict(**m['locales'][actual], category=m['category'], date=m['date'], draft=m['draft'], lang=actual, available=labels, href=f"../{actual}/writing/{a['slug']}.html"))
        for key, title in UI[lang]['nav'].items():
            alternatives = {code: f'../{code}/{key}.html' for code in LANGS}
            page = env.get_template('page.html').render(site=site, lang=lang, ui=UI[lang], preview=preview, active=key, root='../', alternatives=alternatives, title=site['name'] if key == 'index' else title, description=site['profile'][lang], math=False, articles=listings, working_papers=[a for a in listings if a['category'] == 'paper'])
            outputs[f'{lang}/{key}.html'] = page.encode('utf-8')
        for a in entries:
            m = a['meta']
            if lang not in m['locales']:
                continue
            body, toc = render_body(a, lang)
            alternatives = {code: f"../../{code}/writing/{a['slug']}.html" for code in m['locales']}
            page = env.get_template('article.html').render(site=site, lang=lang, ui=UI[lang], preview=preview, active='writing', root='../../', alternatives=alternatives, title=m['locales'][lang]['title'], description=m['locales'][lang]['summary'], math=m.get('math', False), author=m.get('author', site['name']), date=m['date'], category=m['category'], version=m.get('version', ''), draft=m['draft'], stale=a['stale'][lang], body=body, toc=toc)
            outputs[f"{lang}/writing/{a['slug']}.html"] = page.encode('utf-8')
            for asset in (a['folder'] / 'shared').rglob('*'):
                if asset.is_file():
                    outputs[f"{lang}/writing/shared/{a['slug']}/{asset.relative_to(a['folder'] / 'shared').as_posix()}"] = asset.read_bytes()
    outputs['index.html'] = env.get_template('landing.html').render(site=site, preview=preview).encode('utf-8')
    # Canonical URLs and alternate-language URLs are absolute on published pages.
    canonical_pages = [name for name in outputs if name.endswith('.html')]
    for name in canonical_pages:
        page = outputs[name].decode('utf-8')
        canonical = SITE_URL if name == 'index.html' else SITE_URL + name
        page = page.replace('</head>', f'<link rel="canonical" href="{canonical}">\n</head>')
        page = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href=")([^"]+)', lambda m:m[1]+urljoin(SITE_URL+name,m[2]), page)
        outputs[name] = page.encode('utf-8')
    for old, new in LEGACY_REDIRECTS.items():
        outputs[old] = env.get_template('redirect.html').render(target=SITE_URL+new).encode('utf-8')
    outputs['404.html'] = env.get_template('not-found.html').render().encode('utf-8')
    outputs['sitemap.xml'] = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(SITE_URL if p=='index.html' else SITE_URL+p)+'</loc></url>' for p in canonical_pages if not preview or '/writing/' not in p)+'</urlset>').encode('utf-8')
    outputs['robots.txt'] = ('User-agent: *\n'+('Disallow: /\n' if preview else 'Allow: /\nSitemap: '+SITE_URL+'sitemap.xml\n')).encode('utf-8')
    outputs['.nojekyll'] = b''
    # Only remove obsolete files that this builder previously generated.
    # Do not recursively delete directories or touch unrelated files.
    dist = (project / 'dist').resolve()
    manifest = dist / '.generated.json'
    old = read_json(manifest) if manifest.exists() else []
    for name in set(old) - set(outputs):
        target = (dist / safe_relative(name)).resolve()
        if not target.is_relative_to(dist):
            raise ValueError('Output outside dist')
        if target.is_file():
            target.unlink()
    for name, data in outputs.items():
        if name.endswith(('.html', '.xml', '.txt')):
            data = ('\n'.join(line.rstrip() for line in data.decode('utf-8').splitlines())+'\n').encode('utf-8')
        target = dist / safe_relative(name)
        if not target.resolve().is_relative_to(dist):
            raise ValueError('Output outside dist')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    manifest.write_text(json.dumps(sorted(outputs), indent=2), encoding='utf-8')
    return dict(files=len(outputs), articles=len(entries), warnings=warnings)

def new_article(slug, language, title):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Use a lowercase-hyphenated slug')
    folder = BASE / 'content/articles' / slug
    folder.mkdir(parents=True, exist_ok=False)
    meta = dict(source_language=language, category='note', date=date.today().isoformat(), draft=True, locales={language: dict(title=title, summary=title)})
    (folder / 'meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    (folder / f'{language}.md').write_text('## ' + ('本文' if language == 'ja' else 'Content') + '\n\n', encoding='utf-8')
    print(folder)

def review_translation(slug, language):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Invalid slug')
    folder = BASE / 'content/articles' / slug
    meta = read_json(folder / 'meta.json')
    if language == meta['source_language'] or language not in meta['locales'] or not (folder / f'{language}.md').exists():
        raise ValueError('Choose an existing translation')
    meta.setdefault('reviewed', {})[language] = fingerprint(folder, meta)
    (folder / 'meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Recorded review: {slug}/{language}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--preview', action='store_true')
    parser.add_argument('--strict-translations', action='store_true')
    sub = parser.add_subparsers(dest='command')
    new = sub.add_parser('new')
    new.add_argument('slug'); new.add_argument('--lang', choices=LANGS, required=True); new.add_argument('--title', required=True)
    review = sub.add_parser('review-translation')
    review.add_argument('slug'); review.add_argument('--lang', choices=LANGS, required=True)
    args = parser.parse_args()
    if args.command == 'new':
        new_article(args.slug, args.lang, args.title)
    elif args.command == 'review-translation':
        review_translation(args.slug, args.lang)
    else:
        print(json.dumps(build(preview=args.preview, strict_translations=args.strict_translations), ensure_ascii=False, indent=2))
