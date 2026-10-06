"""Build an English static site with articles in their original language. Python 3.11+; no server runtime."""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import sys
from datetime import date, datetime, timezone
from urllib.parse import urljoin

SITE_URL = 'https://daikikumakura.github.io/'
NAV = dict(home='Home', profile='Profile', writing='Writing', software='Software', publication='Publication', activity='Activity')
ILLUSTRATION_ALT = {
    'home': 'Data processing and quantitative modeling illustration',
    'profile': 'Professional research discussion illustration',
    'writing': 'Report analysis and technical writing illustration',
    'software': 'Scientific software development illustration',
    'publication': 'Research presentation illustration',
    'activity': 'Scientific conference illustration',
}
# Retired URLs that still receive search traffic. GitHub Pages cannot send
# HTTP 301, so each becomes an instant meta refresh with a canonical link.
LEGACY_PAGES = {'index':'index.html', 'about':'profile.html', 'publications':'publication.html', 'activities':'activity.html', 'writing':'writing.html', 'software':'software.html'}
LEGACY_REDIRECTS = {'japanese.html':'index.html', 'publication_jpn.html':'publication.html', 'cv.html':'profile.html', 'research.html':'profile.html', 'education.html':'activity.html#teaching', 'gallery.html':'writing.html', 'link.html':'writing.html', 'about.html':'profile.html', 'publications.html':'publication.html', 'activities.html':'activity.html'}
LEGACY_REDIRECTS.update({f'{language}/{old}.html':new for language in ('ja','en') for old,new in LEGACY_PAGES.items()})
RECENT_ON_HOME = 3
FEED_SIZE = 50
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

def validate_site(site):
    for key in ('name','profile','expertise'):
        if not isinstance(site.get(key),str) or not site[key]:raise ValueError('Missing text: '+key)
    for collection in ('software','publications','activities'):
        ids=[row['id'] for row in site[collection]]
        if len(ids)!=len(set(ids)):raise ValueError('Duplicate ID: '+collection)
    for row in site['software']:
        for key in ('status','description','note'):
            if not isinstance(row.get(key),str) or not row[key]:raise ValueError('Missing software text')
    for row in site['activities']:
        if row['category'] not in UI['en']['activity_types']:raise ValueError('Unknown activity category')
    for row in site['publications']:
        if row['kind'] not in UI['en']['publication_types']:raise ValueError('Unknown publication kind')
    for topic in site.get('analysis_topics',[]):
        if not topic.get('label') or not topic.get('articles'):raise ValueError('Invalid analysis topic')


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

def load_articles(content, preview=False, now=None):
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("Article publication time must include a timezone")
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
        if meta.get('updated') is not None and date.fromisoformat(meta['updated']) < date.fromisoformat(meta['date']):
            raise ValueError(f'updated is before date: {folder.name}')
        if meta['source_language'] not in meta['locales']:
            raise ValueError('Original language is missing')
        if meta.get('english') is not None and (meta['source_language'] == 'en' or not meta['english'].get('title') or not meta['english'].get('summary')):
            raise ValueError(f'english needs a title and summary for a non-English original: {folder.name}')
        for lang, data in meta['locales'].items():
            if lang not in LANGS or not data.get('title') or not data.get('summary'):
                raise ValueError(f'Invalid article locale: {folder.name}/{lang}')
            findings = data.get('key_findings', [])
            if not isinstance(findings, list) or len(findings) > 5 or not all(isinstance(x, str) and x.strip() for x in findings):
                raise ValueError(f'key_findings must be up to five non-empty strings: {folder.name}/{lang}')
            if not (folder / f'{lang}.md').is_file():
                raise ValueError(f'Missing article body: {folder.name}/{lang}.md')
        for path in folder.rglob('*'):
            if path.is_symlink():
                raise ValueError('Symlinks are not supported in article content')
        publish_at = None
        if meta.get('publish_at'):
            publish_at = datetime.fromisoformat(meta['publish_at'])
            if publish_at.tzinfo is None:
                raise ValueError('publish_at must include a timezone')
            if publish_at.date().isoformat() != meta['date']:
                raise ValueError('Publication date must match publish_at local date')
        if not preview and (meta['draft'] or (publish_at and now < publish_at)):
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
    # Protect TeX from Markdown escaping and emphasis outside literal code.
    math_fragments = []
    if article['meta'].get('math', False):
        def protect_math(match):
            token = f'MATHPLACEHOLDER{len(math_fragments)}END'
            math_fragments.append(html.escape(match.group(0)))
            return token
        parts = re.split(r'(```[\s\S]*?```|`[^`\n]*`|<pre>[\s\S]*?</pre>)', body)
        for i in range(0, len(parts), 2):
            parts[i] = re.sub(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]', protect_math, parts[i])
        body = ''.join(parts)
    parser = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'attr_list'])
    rendered = parser.convert(body)
    for i, fragment in enumerate(math_fragments):
        rendered = rendered.replace(f'MATHPLACEHOLDER{i}END', '<span class="math">' + fragment + '</span>')
    return rendered, parser.toc

def image_size(path):
    """Intrinsic size of a PNG or SVG figure, or None."""
    data = path.read_bytes()
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return int.from_bytes(data[16:20], 'big'), int.from_bytes(data[20:24], 'big')
    if path.suffix.lower() == '.svg':
        head = data[:4000].decode('utf-8', 'ignore')
        root = re.search(r'<svg\b[^>]*>', head)
        if root:
            w = re.search(r'\swidth="([\d.]+)(?:px|pt)?"', root[0]); h = re.search(r'\sheight="([\d.]+)(?:px|pt)?"', root[0])
            if w and h:
                return round(float(w[1])), round(float(h[1]))
            box = re.search(r'viewBox="[\d.\-]+[ ,]+[\d.\-]+[ ,]+([\d.]+)[ ,]+([\d.]+)"', root[0])
            if box:
                return round(float(box[1])), round(float(box[2]))
    return None

def add_image_attributes(body, article):
    """Reserve figure space (no layout shift) and lazy-load all but the first figure."""
    shared = article['folder'] / 'shared'
    count = 0
    def attributes(match):
        nonlocal count
        tag, src = match[0], html.unescape(match[1])
        prefix = 'shared/' + article['slug'] + '/'
        extra = ''
        if src.startswith(prefix) and 'width=' not in tag:
            path = shared / safe_relative(src[len(prefix):])
            size = image_size(path) if path.is_file() else None
            if size:
                extra += f' width="{size[0]}" height="{size[1]}"'
        if 'loading=' not in tag and count:
            extra += ' loading="lazy"'
        if 'decoding=' not in tag:
            extra += ' decoding="async"'
        count += 1
        return re.sub(r'\s*/?>$', extra + ' />', tag, count=1)
    return re.sub(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*>', attributes, body)

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
    # Retain the public paths of legacy resources and verification files.
    for asset in (project / 'static').rglob('*'):
        if asset.is_file():
            outputs[asset.relative_to(project / 'static').as_posix()] = asset.read_bytes()
    for asset in (project / 'assets').rglob('*'):
        if asset.is_file():
            outputs['assets/' + asset.relative_to(project / 'assets').as_posix()] = asset.read_bytes()
    from seo import enrich
    ui=dict(UI['en'],nav=NAV)
    listings=[]
    for a in entries:
        m=a['meta']; language=m['source_language']
        listings.append(dict(**m['locales'][language],category=m['category'],date=m['date'],draft=m['draft'],lang=language,available='Japanese' if language=='ja' else 'English',href=f"writing/{a['slug']}.html"))
    # The profile is English: Japanese originals show their English title when one exists.
    def profile_link(a):
        m=a['meta']; english=m.get('english')
        if m['source_language']!='en' and 'en' in m['locales']:
            return dict(title=m['locales']['en']['title'],lang='en',note='',href=f"writing/{a['slug']}-en.html")
        if english:return dict(title=english['title'],lang='en',note='in Japanese',href=f"writing/{a['slug']}.html")
        return dict(title=m['locales'][m['source_language']]['title'],lang=m['source_language'],note='in Japanese' if m['source_language']=='ja' else '',href=f"writing/{a['slug']}.html")
    published={a['slug']:profile_link(a) for a in entries}
    # Unpublished or scheduled articles are left out until they are live.
    analyses=[dict(label=t['label'],articles=[published[s] for s in t['articles'] if s in published]) for t in site.get('analysis_topics',[])]
    analyses=[t for t in analyses if t['articles']]
    def related(slug, limit=5):
        # Other live articles that share an analysis topic, in topic order.
        seen=[]
        for t in site.get('analysis_topics',[]):
            if slug in t['articles']:
                seen+=[s for s in t['articles'] if s!=slug and s in published and s not in seen]
        # Related links point to each original article, titled in its own language.
        source={a['slug']:a['meta'] for a in entries}
        return [dict(href=f"{s}.html",title=source[s]['locales'][source[s]['source_language']]['title'],lang=source[s]['source_language']) for s in seen[:limit]]
    def output(name,page,lang='en',article=None):
        canonical=SITE_URL if name in ('index.html','home.html') else SITE_URL+name
        page=enrich(page,name,site,SITE_URL,article)
        page=page.replace('</head>',f'<link rel="canonical" href="{canonical}">\n</head>')
        outputs[name]=page.encode('utf-8')
    for key,title in NAV.items():
        page=env.get_template('page.html').render(site=site,lang='en',ui=ui,preview=preview,active=key,root='',alternatives={},title=site['name'] if key=='home' else title,description=site['profile'],math=False,articles=listings,recent=listings[:RECENT_ON_HOME],working_papers=[a for a in listings if a['category']=='paper'],analyses=analyses,illustration_alt=ILLUSTRATION_ALT[key])
        output(key+'.html',page)
        if key=='home':outputs['index.html']=outputs['home.html']
    for a in entries:
        m=a['meta']; original=m['source_language']
        alternatives={code:(a['slug']+'.html' if code==original else a['slug']+'-'+code+'.html') for code in m['locales']}
        for language in m['locales']:
            body,toc=render_body(a,language)
            body=add_image_attributes(body,a)
            page=env.get_template('article.html').render(site=site,lang=language,ui=ui,preview=preview,active='writing',root='../',alternatives=alternatives,title=m['locales'][language]['title'],description=m['locales'][language]['summary'],math=m.get('math',False),author=m.get('author',site['name']),date=m['date'],category=m['category'],version=m.get('version',''),draft=m['draft'],stale=a['stale'][language],body=body,toc=toc,key_findings=m['locales'][language].get('key_findings',[]),english=m.get('english') if language!='en' and 'en' not in m['locales'] else None,related=related(a['slug']))
            output('writing/'+alternatives[language],page,language,m)
        for asset in (a['folder']/'shared').rglob('*'):
            if asset.is_file():outputs[f"writing/shared/{a['slug']}/{asset.relative_to(a['folder']/'shared').as_posix()}"]=asset.read_bytes()
    canonical_pages=['index.html']+[key+'.html' for key in NAV if key!='home']+[name for name in outputs if name.startswith('writing/') and name.endswith('.html')]
    if not preview:
        for old,new in LEGACY_REDIRECTS.items():
            if old in outputs:raise ValueError('Redirect would replace a page: '+old)
            outputs[old]=env.get_template('redirect.html').render(target=SITE_URL+new).encode('utf-8')
    outputs['404.html']=env.get_template('not-found.html').render().encode('utf-8')
    # lastmod only where the date is known: articles (publication or update
    # date) and the pages that list them (newest article). Other pages carry
    # no lastmod rather than an inaccurate one.
    lastmod={}
    for a in entries:
        m=a['meta']; changed=m.get('updated') or m['date']
        for code in m['locales']:
            lastmod['writing/'+(a['slug']+'.html' if code==m['source_language'] else a['slug']+'-'+code+'.html')]=changed
    if entries:
        newest=max(a['meta'].get('updated') or a['meta']['date'] for a in entries)
        lastmod['index.html']=lastmod['writing.html']=newest
    def sitemap_url(p):
        tag='<url><loc>'+html.escape(SITE_URL if p=='index.html' else SITE_URL+p)+'</loc>'
        if p in lastmod:tag+='<lastmod>'+lastmod[p]+'</lastmod>'
        return tag+'</url>'
    outputs['sitemap.xml']=('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(sitemap_url(p) for p in canonical_pages if not preview or not p.startswith('writing/'))+'</urlset>').encode('utf-8')
    if not preview:
        outputs['feed.xml']=atom_feed(site,entries)
    outputs['robots.txt']=('User-agent: *\n'+('Disallow: /\n' if preview else 'Allow: /\nSitemap: '+SITE_URL+'sitemap.xml\nSitemap: '+SITE_URL+'feed.xml\n')).encode('utf-8')
    if not preview:
        outputs['llms.txt']=llms_txt(site,entries)
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

def llms_txt(site, entries):
    """Plain-text site guide (llmstxt.org format) listing pages and live articles."""
    lines=['# '+site['name']+' ('+site['alternate_name']+')','','> '+site['profile'],'',site['expertise'],'','## Pages','']
    for key,label in NAV.items():
        page=SITE_URL if key=='home' else SITE_URL+key+'.html'
        lines.append(f'- [{label}]({page})')
    lines+=['','## Writing','']
    for a in entries:
        m=a['meta']; loc=m['locales'][m['source_language']]; english=m.get('english')
        if m['source_language']!='en' and 'en' in m['locales']:
            en=m['locales']['en']
            lines.append(f"- [{en['title']}]({SITE_URL}writing/{a['slug']}-en.html) (English translation; original in Japanese: {SITE_URL}writing/{a['slug']}.html): {en['summary']}")
            continue
        title=english['title'] if english else loc['title']; summary=english['summary'] if english else loc['summary']
        note=' (article in Japanese)' if m['source_language']=='ja' else ''
        lines.append(f"- [{title}]({SITE_URL}writing/{a['slug']}.html){note}: {summary}")
    return ('\n'.join(lines)+'\n').encode('utf-8')

def atom_time(meta):
    if meta.get('updated'):
        return meta['updated']+'T00:00:00+09:00'
    if meta.get('publish_at'):
        return datetime.fromisoformat(meta['publish_at']).isoformat()
    return meta['date']+'T00:00:00+09:00'

def atom_feed(site, entries):
    """Atom feed of published articles (also accepted by search engines as a sitemap)."""
    items=[]
    for a in entries[:FEED_SIZE]:
        m=a['meta']; lang=m['source_language']; loc=m['locales'][lang]
        url=SITE_URL+'writing/'+a['slug']+'.html'
        published=datetime.fromisoformat(m['publish_at']).isoformat() if m.get('publish_at') else m['date']+'T00:00:00+09:00'
        items.append('<entry><title>'+html.escape(loc['title'])+'</title><link rel="alternate" type="text/html" href="'+url+'"/><id>'+url+'</id>'
                     '<published>'+published+'</published><updated>'+atom_time(m)+'</updated><summary xml:lang="'+lang+'">'+html.escape(loc['summary'])+'</summary></entry>')
    updated=max((atom_time(a['meta']) for a in entries),default='2026-01-01T00:00:00+09:00')
    head=('<?xml version="1.0" encoding="UTF-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom"><title>Writing | '+html.escape(site['name'])+'</title>'
          '<link rel="self" type="application/atom+xml" href="'+SITE_URL+'feed.xml"/><link rel="alternate" type="text/html" href="'+SITE_URL+'writing.html"/>'
          '<id>'+SITE_URL+'feed.xml</id><updated>'+updated+'</updated><author><name>'+html.escape(site['name'])+'</name><uri>'+SITE_URL+'</uri></author>')
    return (head+''.join(items)+'</feed>').encode('utf-8')

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

