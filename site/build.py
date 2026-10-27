"""Build an English static site with articles in their original language. Python 3.11+; no server runtime."""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import sys
import unicodedata
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
# Documentation sites published under this domain by other repositories (pkgdown) with their own sitemaps.
EXTRA_SITEMAPS = ('rsemflow/sitemap.xml',)
# Reference pages (tools, glossary terms, catalogs): one folder per page in content/reference,
# written in both languages. English is the default file name, Japanese ends in -ja.
REFERENCE_KINDS = {'tool': 'tools', 'term': 'glossary', 'catalog': 'catalog'}
REFERENCE_HEADINGS = {'tool': 'Tools', 'term': 'Glossary', 'catalog': 'Catalogs'}
REFERENCE_LABELS = {'tool': 'Tool', 'term': 'Glossary term', 'catalog': 'Catalog'}
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
    software_slugs=[]
    for row in site['software']:
        if 'slug' in row:
            summary=row.get('summary','')
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',row['slug']) or not row.get('headline') or not 60<=len(summary)<=160:
                raise ValueError('A software page needs a slug, a headline and a 60-160 character summary: '+row['id'])
            software_slugs.append(row['slug'])
    if len(software_slugs)!=len(set(software_slugs)):raise ValueError('Duplicate software slug')
    for row in site['activities']:
        if row['category'] not in UI['en']['activity_types']:raise ValueError('Unknown activity category')
    for row in site['publications']:
        if row['kind'] not in UI['en']['publication_types']:raise ValueError('Unknown publication kind')
    topic_slugs=[]
    for topic in site.get('analysis_topics',[]):
        if not topic.get('label') or not topic.get('articles'):raise ValueError('Invalid analysis topic')
        if 'slug' in topic:
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',topic['slug']) or not topic.get('description'):raise ValueError('A topic page needs a lowercase-hyphenated slug and a description: '+topic['label'])
            topic_slugs.append(topic['slug'])
    if len(topic_slugs)!=len(set(topic_slugs)):raise ValueError('Duplicate topic slug')


def fingerprint(folder, meta):
    """Original title, summary, body, and all shared assets form one revision.

    CRLF is normalized so a review recorded on Windows matches the LF checkout in CI."""
    source = meta['source_language']
    digest = hashlib.sha256()
    # Search-result text is not article content: editing it must not unreview a translation.
    original = {k: v for k, v in meta['locales'][source].items() if k not in ('seo_title', 'seo_description')}
    digest.update(json.dumps(original, sort_keys=True, ensure_ascii=False).encode())
    digest.update((folder / f'{source}.md').read_bytes().replace(b'\r\n', b'\n'))
    # Sort by POSIX string: Windows paths compare case-insensitively, Linux paths do not.
    for path in sorted((folder / 'shared').rglob('*'), key=lambda p: p.relative_to(folder).as_posix()):
        if path.is_file():
            digest.update(path.relative_to(folder).as_posix().encode())
            digest.update(path.read_bytes().replace(b'\r\n', b'\n'))
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
            for key in ('seo_title', 'seo_description'):
                if key in data and (not isinstance(data[key], str) or not data[key].strip()):
                    raise ValueError(f'{key} must be a non-empty string: {folder.name}/{lang}')
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
            # Dollar delimiters are rewritten to \( \) and \[ \], the only ones MathJax is configured for.
            if match.group('display') is not None:
                tex = '\\[' + match.group('display') + '\\]'
            elif match.group('inline') is not None:
                tex = '\\(' + match.group('inline') + '\\)'
            else:
                tex = match.group(0)
            token = f'MATHPLACEHOLDER{len(math_fragments)}END'
            math_fragments.append(html.escape(tex))
            return token
        math_pattern = re.compile(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|\$\$(?P<display>[\s\S]+?)\$\$'
                                  r'|(?<![\\$])\$(?P<inline>[^\s$](?:[^$\n]*?[^\s$])?)\$(?![$\d])')
        parts = re.split(r'(```[\s\S]*?```|`[^`\n]*`|<pre>[\s\S]*?</pre>)', body)
        for i in range(0, len(parts), 2):
            parts[i] = math_pattern.sub(protect_math, parts[i])
        body = ''.join(parts)
    parser = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'attr_list'])
    rendered = parser.convert(body)
    for i, fragment in enumerate(math_fragments):
        rendered = rendered.replace(f'MATHPLACEHOLDER{i}END', '<span class="math">' + fragment + '</span>')
    from citations import link_numbered_references
    rendered = link_numbered_references(rendered)
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

def display_width(text):
    """Width in half-width cells: full-width (CJK) characters count twice."""
    return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in text)

def load_reference(content, article_slugs):
    """Reference pages: interactive tools, glossary terms and catalogs, each in Japanese and English."""
    entries = []
    for folder in sorted((content / 'reference').glob('*')):
        if not folder.is_dir():
            continue
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', folder.name):
            raise ValueError(f'Invalid reference slug: {folder.name}')
        meta = read_json(folder / 'meta.json')
        if meta.get('kind') not in REFERENCE_KINDS:
            raise ValueError(f'Invalid reference kind: {folder.name}')
        date.fromisoformat(meta['updated'])
        if set(meta['locales']) != {'ja', 'en'}:
            raise ValueError(f'A reference page needs both ja and en: {folder.name}')
        for lang, data in meta['locales'].items():
            for key in ('title', 'summary', 'seo_title', 'seo_description'):
                if not isinstance(data.get(key), str) or not data[key].strip():
                    raise ValueError(f'Missing {key}: {folder.name}/{lang}')
            for item in data.get('faq', []):
                if not item.get('q') or not item.get('a'):
                    raise ValueError(f'A question needs q and a: {folder.name}/{lang}')
            if not (folder / f'{lang}.md').is_file():
                raise ValueError(f'Missing body: {folder.name}/{lang}.md')
        for slug in meta.get('related_articles', []):
            if slug not in article_slugs:
                raise ValueError(f'Unknown related article {slug}: {folder.name}')
        entries.append(dict(meta=meta, folder=folder, slug=folder.name, kind=meta['kind']))
    return entries

def reference_file(entry, lang):
    return f"{REFERENCE_KINDS[entry['kind']]}/{entry['slug']}" + ('-ja' if lang == 'ja' else '') + '.html'

def reference_warnings(entries):
    notes = []
    for e in entries:
        for lang, data in e['meta']['locales'].items():
            where = f"{reference_file(e, lang)}"
            if display_width(data['seo_title']) > 60:
                notes.append(f"Title is cut in search results ({display_width(data['seo_title'])} cells > 60): {where}")
            description = data['seo_description']
            if display_width(description) > 200 if lang == 'ja' else len(description) > 160:
                notes.append(f'Description is cut in search results ({len(description)} characters): {where}')
    return notes

def seo_warnings(entries, site_name):
    """Advisory checks of search-result text; they never fail a build.

    A title is cut at about 60 half-width cells and a description at about 160, so
    the effective title (seo_title, or the title plus the site name) is measured."""
    notes = []
    for a in entries:
        for lang, data in a['meta']['locales'].items():
            title = data.get('seo_title') or f"{data['title']} | {site_name}"
            description = data.get('seo_description') or data['summary']
            where = f"{a['slug']}/{lang}"
            if display_width(title) > 60:
                notes.append(f'Title is cut in search results ({display_width(title)} cells > 60): {where}')
            if display_width(description) > 200 if lang == 'ja' else len(description) > 160:
                notes.append(f'Description is cut in search results ({len(description)} characters): {where}')
            elif len(description) < (40 if lang == 'ja' else 70):
                notes.append(f'Description is very short ({len(description)} characters): {where}')
        if not (a['folder'] / 'og.png').is_file():
            notes.append(f"No social card (og.png); the first figure, or the site card if there is none, is used: {a['slug']}")
    return notes

def build(project=BASE, preview=False, strict_translations=False):
    project = Path(project)
    site = read_json(project / 'content/site.json')
    validate_site(site)
    entries = load_articles(project / 'content', preview)
    reference = load_reference(project / 'content', {p.name for p in (project / 'content/articles').iterdir() if p.is_dir()})
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
        versions=[dict(lang=code,href=f"writing/{a['slug']}{'' if code==language else '-'+code}.html") for code in m['locales']]
        listings.append(dict(**m['locales'][language],category=m['category'],date=m['date'],draft=m['draft'],lang=language,available='Japanese' if language=='ja' else 'English',href=f"writing/{a['slug']}.html",versions=versions))
    # The profile is English: Japanese originals show their English title when one exists.
    def profile_link(a):
        m=a['meta']; english=m.get('english')
        if m['source_language']!='en' and 'en' in m['locales']:
            return dict(title=m['locales']['en']['title'],lang='en',note='',href=f"writing/{a['slug']}-en.html")
        if english:return dict(title=english['title'],lang='en',note='in Japanese',href=f"writing/{a['slug']}.html")
        return dict(title=m['locales'][m['source_language']]['title'],lang=m['source_language'],note='in Japanese' if m['source_language']=='ja' else '',href=f"writing/{a['slug']}.html")
    published={a['slug']:profile_link(a) for a in entries}
    # Unpublished or scheduled articles are left out until they are live.
    hubs={}
    for t in site.get('analysis_topics',[]):
        live=[x for x in t['articles'] if x in published]
        if live and t.get('slug'):hubs[t['slug']]=dict(label=t['label'],slug=t['slug'],href=f"topics/{t['slug']}.html",description=t['description'],articles=live)
    analyses=[dict(label=t['label'],href=(f"topics/{t['slug']}.html" if t.get('slug') in hubs else None),articles=[published[s] for s in t['articles'] if s in published]) for t in site.get('analysis_topics',[])]
    analyses=[t for t in analyses if t['articles']]
    def article_hubs(slug):
        return [dict(label=h['label'],href='../'+h['href']) for h in hubs.values() if slug in h['articles']]
    def article_topics(slug):
        return [h['label'] for h in hubs.values() if slug in h['articles']]
    def shown(a):
        """How a topic page presents an article: English title and summary when they exist.

        lang describes the title and summary; findings_lang describes the key findings."""
        m=a['meta']; src=m['source_language']
        if src!='en' and 'en' in m['locales']:
            loc=m['locales']['en']
            return dict(title=loc['title'],summary=loc['summary'],findings=loc.get('key_findings',[]),href=f"writing/{a['slug']}-en.html",lang='en',findings_lang='en',note='English translation of a Japanese article',date=m['date'],category=m['category'])
        loc=m['locales'][src]; english=m.get('english')
        return dict(title=(english or loc)['title'],summary=(english or loc)['summary'],findings=loc.get('key_findings',[]),href=f"writing/{a['slug']}.html",lang='en' if english else src,findings_lang=src,note='article in Japanese' if src=='ja' else '',date=m['date'],category=m['category'])
    def cite_text(m,title,file):
        english=m['locales'].get('en') or m.get('english')
        citation_title=english['title'] if english else title
        language_note=' [Article in Japanese]' if 'en' not in m['locales'] else ''
        if 'en' in m['locales']:
            file=file.removesuffix('-ja.html').removesuffix('-en.html').removesuffix('.html')+('' if m['source_language']=='en' else '-en')+'.html'
        return f"Kumakura, D. ({m['date'][:4]}). {citation_title}{language_note}. daikikumakura.github.io. {SITE_URL}writing/{file}"
    def related(slug, limit=5):
        # Other live articles that share an analysis topic, in topic order.
        seen=[]
        for t in site.get('analysis_topics',[]):
            if slug in t['articles']:
                seen+=[s for s in t['articles'] if s!=slug and s in published and s not in seen]
        # Related links point to each original article, titled in its own language.
        source={a['slug']:a['meta'] for a in entries}
        return [dict(href=f"{s}.html",title=source[s]['locales'][source[s]['source_language']]['title'],lang=source[s]['source_language']) for s in seen[:limit]]
    def output(name,page,lang='en',article=None,og_image=None,topics=None):
        canonical=SITE_URL if name in ('index.html','home.html') else SITE_URL+name
        page=enrich(page,name,site,SITE_URL,article,og_image,topics)
        page=page.replace('</head>',f'<link rel="canonical" href="{canonical}">\n</head>')
        outputs[name]=page.encode('utf-8')
    for key,title in NAV.items():
        topic_map=[dict(label=h['label'],href=h['href'],articles=[dict(title=published[s]['title'],href=published[s]['href'],lang=published[s]['lang']) for s in h['articles']]) for h in hubs.values()]
        page=env.get_template('page.html').render(site=site,lang='en',ui=ui,preview=preview,active=key,root='',alternatives={},title=site['name'] if key=='home' else title,description=site['profile'],math=False,articles=listings,recent=listings[:RECENT_ON_HOME],working_papers=[a for a in listings if a['category']=='paper'],analyses=analyses,hubs=list(hubs.values()),topic_map=topic_map,illustration_alt=ILLUSTRATION_ALT[key])
        output(key+'.html',page)
        if key=='home':outputs['index.html']=outputs['home.html']
    for a in entries:
        m=a['meta']; original=m['source_language']
        # The 1200x630 social card sits beside the article, not in shared/, so it is
        # published only with the article and never changes a translation's revision.
        card=a['folder']/'og.png'
        og_card=f"writing/og/{a['slug']}.png" if card.is_file() else None
        if og_card:outputs[og_card]=card.read_bytes()
        alternatives={code:(a['slug']+'.html' if code==original else a['slug']+'-'+code+'.html') for code in m['locales']}
        for language in m['locales']:
            body,toc=render_body(a,language)
            body=add_image_attributes(body,a)
            page=env.get_template('article.html').render(site=site,lang=language,ui=ui,preview=preview,active='writing',root='../',alternatives=alternatives,title=m['locales'][language]['title'],description=m['locales'][language]['summary'],math=m.get('math',False),author=m.get('author',site['name']),date=m['date'],category=m['category'],version=m.get('version',''),draft=m['draft'],stale=a['stale'][language],body=body,toc=toc,key_findings=m['locales'][language].get('key_findings',[]),english=m.get('english') if language!='en' and 'en' not in m['locales'] else None,related=related(a['slug']),hubs=article_hubs(a['slug']),cite=cite_text(m,m['locales'][language]['title'],alternatives[language]))
            output('writing/'+alternatives[language],page,language,m,og_card,article_topics(a['slug']))
        for asset in (a['folder']/'shared').rglob('*'):
            if asset.is_file():outputs[f"writing/shared/{a['slug']}/{asset.relative_to(a['folder']/'shared').as_posix()}"]=asset.read_bytes()
    for h in hubs.values():
        items=[shown(a) for x in h['articles'] for a in entries if a['slug']==x]
        page=env.get_template('topic.html').render(site=site,lang='en',ui=ui,preview=preview,active='writing',root='../',alternatives={},title=h['label'],description=h['description'],math=False,hub=h,items=items)
        output(h['href'],page)
    for sw in site['software']:
        if 'slug' not in sw:continue
        related_live=[published[x] for x in sw.get('related_articles',[]) if x in published]
        page=env.get_template('software-page.html').render(site=site,lang='en',ui=ui,preview=preview,active='software',root='../',alternatives={},title=sw['headline'],description=sw['summary'],math=False,sw=sw,related=related_live)
        output(f"software/{sw['slug']}.html",page)
    live_source={a['slug']:a['meta'] for a in entries}
    def reference_links(slugs,language):
        # Live articles only, in the page's language when the article has it.
        links=[]
        for slug in slugs:
            if slug not in live_source:continue
            m=live_source[slug]; code=language if language in m['locales'] else m['source_language']
            links.append(dict(href=f"{slug}.html" if code==m['source_language'] else f"{slug}-{code}.html",title=m['locales'][code]['title'],lang=code))
        return links
    for e in reference:
        m=e['meta']
        alternatives={code:reference_file(e,code).split('/',1)[1] for code in ('en','ja')}
        for language in ('en','ja'):
            loc=m['locales'][language]
            body,toc=render_body(dict(folder=e['folder'],meta=m),language)
            page=env.get_template('reference.html').render(site=site,lang=language,ui=ui,preview=preview,active='writing',root='../',alternatives=alternatives,title=loc['title'],description=loc['summary'],math=m.get('math',False),body=body,faq=loc.get('faq',[]),related=reference_links(m.get('related_articles',[]),language),kind=REFERENCE_HEADINGS[e['kind']],updated=m['updated'])
            output(reference_file(e,language),page,language,m)
    groups=[dict(heading=REFERENCE_HEADINGS[kind],items=[dict(en=e['meta']['locales']['en'],ja=e['meta']['locales']['ja'],en_href=reference_file(e,'en'),ja_href=reference_file(e,'ja')) for e in reference if e['kind']==kind]) for kind in REFERENCE_KINDS]
    groups=[g for g in groups if g['items']]
    output('reference.html',env.get_template('reference-index.html').render(site=site,lang='en',ui=ui,preview=preview,active='writing',root='',alternatives={},title='Tools and reference',description='Interactive tools, a glossary of pharmacometrics terms and catalogs that accompany the analyses by Daiki Kumakura, in Japanese and English.',math=False,groups=groups))
    canonical_pages=['index.html']+[key+'.html' for key in NAV if key!='home']+[name for name in outputs if name.startswith(('writing/','topics/','software/','tools/','glossary/','catalog/','reference.html')) and name.endswith('.html')]
    if not preview:
        for old,new in LEGACY_REDIRECTS.items():
            if old in outputs:raise ValueError('Redirect would replace a page: '+old)
            outputs[old]=env.get_template('redirect.html').render(target=SITE_URL+new,source=old).encode('utf-8')
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
    for e in reference:
        for code in ('en','ja'):lastmod[reference_file(e,code)]=e['meta']['updated']
    if reference:lastmod['reference.html']=max(e['meta']['updated'] for e in reference)
    for h in hubs.values():
        lastmod[h['href']]=max(a['meta'].get('updated') or a['meta']['date'] for a in entries if a['slug'] in h['articles'])
    def sitemap_url(p):
        tag='<url><loc>'+html.escape(SITE_URL if p=='index.html' else SITE_URL+p)+'</loc>'
        if p in lastmod:tag+='<lastmod>'+lastmod[p]+'</lastmod>'
        for a in entries:
            m=a['meta']; files={code:'writing/'+a['slug']+('' if code==m['source_language'] else '-'+code)+'.html' for code in m['locales']}
            if p not in files.values() or len(files)<2:continue
            for code,name in files.items():tag+='<xhtml:link rel="alternate" hreflang="'+code+'" href="'+html.escape(SITE_URL+name)+'"/>'
            if 'en' in files:tag+='<xhtml:link rel="alternate" hreflang="x-default" href="'+html.escape(SITE_URL+files['en'])+'"/>'
        return tag+'</url>'
    outputs['sitemap.xml']=('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+''.join(sitemap_url(p) for p in canonical_pages if not preview or not p.startswith('writing/'))+'</urlset>').encode('utf-8')
    if not preview:
        outputs['feed.xml']=atom_feed(site,entries)
    outputs['robots.txt']=('User-agent: *\n'+('Disallow: /\n' if preview else 'Allow: /\nSitemap: '+SITE_URL+'sitemap.xml\nSitemap: '+SITE_URL+'feed.xml\n'+''.join('Sitemap: '+SITE_URL+path+'\n' for path in EXTRA_SITEMAPS))).encode('utf-8')
    if not preview:
        outputs['llms.txt']=llms_txt(site,entries,list(hubs.values()),reference)
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
    return dict(files=len(outputs), articles=len(entries), warnings=warnings, seo_warnings=seo_warnings(entries, site['name'])+reference_warnings(reference))

def llms_txt(site, entries, hubs=(), reference=()):
    """Plain-text site guide (llmstxt.org format) for language models and agents.

    It restates the third-person summary, the identities that belong to the same person,
    the topic pages, and every live article with its key findings."""
    names = ', '.join(site.get('alternate_names', [site['alternate_name']]))
    lines = ['# ' + site['name'] + ' (' + site['alternate_name'] + ')', '', '> ' + site.get('bio', site['profile']), '',
             'Also written as: ' + names + '. All analyses use public data or simulation only and are not clinical or regulatory work.', '',
             '## Identity', '',
             f"- ORCID: {site['orcid']}", f"- Google Scholar: {site['scholar']}", f"- GitHub: {site['github']}", f"- Qiita: {site['qiita']}", f"- LinkedIn: {site['linkedin']}", '',
             '## Pages', '']
    for key, label in NAV.items():
        page = SITE_URL if key == 'home' else SITE_URL + key + '.html'
        lines.append(f'- [{label}]({page})')
    if hubs:
        lines += ['', '## Topics', '']
        lines += [f"- [{h['label']}]({SITE_URL}{h['href']}): {h['description']}" for h in hubs]
    pages = [x for x in site['software'] if 'slug' in x]
    if pages:
        lines += ['', '## Software', '']
        lines += [f"- [{x['id']}]({SITE_URL}software/{x['slug']}.html): {x['summary']} Repository: {x['url']}" for x in pages]
    if reference:
        lines += ['', '## Tools and reference', '', f'- [All tools and reference pages]({SITE_URL}reference.html)']
        for e in reference:
            en = e['meta']['locales']['en']
            lines.append(f"- [{en['title']}]({SITE_URL}{reference_file(e, 'en')}) ({REFERENCE_LABELS[e['kind']]}; Japanese: {SITE_URL}{reference_file(e, 'ja')}): {en['summary']}")
    lines += ['', '## Writing', '']
    for a in entries:
        m = a['meta']; loc = m['locales'][m['source_language']]; english = m.get('english')
        if m['source_language'] != 'en' and 'en' in m['locales']:
            en = m['locales']['en']
            lines.append(f"- [{en['title']}]({SITE_URL}writing/{a['slug']}-en.html) (English translation; original in Japanese: {SITE_URL}writing/{a['slug']}.html): {en['summary']}")
            findings = en.get('key_findings', [])
        else:
            title = english['title'] if english else loc['title']; summary = english['summary'] if english else loc['summary']
            note = ' (article in Japanese)' if m['source_language'] == 'ja' else ''
            lines.append(f"- [{title}]({SITE_URL}writing/{a['slug']}.html){note}: {summary}")
            findings = loc.get('key_findings', []) if m['source_language'] == 'en' else []
        lines += ['  - Key finding: ' + f for f in findings]
    return ('\n'.join(lines) + '\n').encode('utf-8')

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

