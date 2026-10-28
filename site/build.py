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
# Retired URLs that still receive search traffic. GitHub Pages cannot send
# HTTP 301, so each becomes an instant meta refresh with a canonical link.
LEGACY_PAGES = {'index':'index.html', 'about':'profile.html', 'publications':'publication.html', 'activities':'activity.html', 'writing':'writing.html', 'software':'software.html'}
LEGACY_REDIRECTS = {'japanese.html':'index.html', 'publication_jpn.html':'publication.html', 'cv.html':'profile.html', 'research.html':'profile.html', 'education.html':'activity.html#teaching', 'gallery.html':'writing.html', 'link.html':'writing.html', 'about.html':'profile.html', 'publications.html':'publication.html', 'activities.html':'activity.html'}
LEGACY_REDIRECTS.update({f'{language}/{old}.html':new for language in ('ja','en') for old,new in LEGACY_PAGES.items()})
# Documentation sites published under this domain by other repositories (pkgdown) with their own sitemaps.
EXTRA_SITEMAPS = ('rsemflow/sitemap.xml',)
# Reference pages (tools, glossary terms, catalogs): one folder per page in content/reference,
# written in both languages. English is the default file name, Japanese ends in -ja.
REFERENCE_KINDS = {'policy': 'about', 'tool': 'tools', 'term': 'glossary', 'catalog': 'catalog'}
REFERENCE_HEADINGS = {'policy': 'About these analyses', 'tool': 'Tools', 'term': 'Glossary', 'catalog': 'Catalogs'}
REFERENCE_LABELS = {'policy': 'About page', 'tool': 'Tool', 'term': 'Glossary term', 'catalog': 'Catalog'}
# The Writing index exists once per language so that every title on a page is in that page's language.
WRITING_ALTERNATIVES = {'en': 'writing.html', 'ja': 'writing-ja.html'}
WRITING_TITLE_JA = '記事一覧'
WRITING_DESCRIPTION_JA = '熊倉大騎による、公開データの解析、技術メモ、チュートリアルの一覧（日本語）。母集団PK、PK/PD、用量選択、腫瘍動態などを扱う。各記事に英語版へのリンクがある。'
WRITING_LEAD = {'en': 'This is the English list. Each article is also available in Japanese; the link under each entry opens the other language.',
                'ja': 'これは日本語の一覧です。各記事の下のリンクから、英語版を開けます。'}
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
    for path in site.get('legacy_topic_paths',[]):
        if not re.fullmatch(r'topics/[a-z0-9]+(?:-[a-z0-9]+)*\.html',path):
            raise ValueError('Invalid legacy topic path: '+path)


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
    # Date-only articles use midnight JST, consistently with the Atom feed.
    return sorted(entries, key=lambda a: (
        datetime.fromisoformat(a['meta'].get('publish_at') or a['meta']['date']+'T00:00:00+09:00'),
        a['slug']), reverse=True)

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
    # The footer links to the page on how the analyses are made once it exists.
    env.globals['about_page'] = 'about/about-these-analyses.html' if any(e['slug'] == 'about-these-analyses' for e in reference) else None
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
        listings.append(dict(**m['locales'][language],slug=a['slug'],category=m['category'],date=m['date'],draft=m['draft'],lang=language,available='Japanese' if language=='ja' else 'English',href=f"writing/{a['slug']}.html",versions=versions))
    def language_listing(a,language):
        """One list entry in a single language: its own title and summary, never the other language's.

        When the article has no version in that language, the English summary of a Japanese
        original is shown with a note; the link then leads to the original."""
        m=a['meta']; original=m['source_language']
        if language in m['locales']:
            loc=m['locales'][language]; lang=language; note=''
            href=f"writing/{a['slug']}.html" if language==original else f"writing/{a['slug']}-{language}.html"
        elif language=='en' and m.get('english'):
            loc=m['english']; lang='en'; note='article in Japanese'; href=f"writing/{a['slug']}.html"
        else:
            loc=m['locales'][original]; lang=original; note='in Japanese' if original=='ja' else ''; href=f"writing/{a['slug']}.html"
        versions=[dict(lang=code,href=f"writing/{a['slug']}{'' if code==original else '-'+code}.html") for code in m['locales'] if code!=lang]
        return dict(title=loc['title'],summary=loc['summary'],slug=a['slug'],category=m['category'],date=m['date'],draft=m['draft'],lang=lang,note=note,available='Japanese' if lang=='ja' else 'English',href=href,versions=versions)
    listings_en=[language_listing(a,'en') for a in entries]
    listings_ja=[language_listing(a,'ja') for a in entries]
    # The profile is English: Japanese originals show their English title when one exists.
    def profile_link(a):
        m=a['meta']; english=m.get('english')
        if m['source_language']!='en' and 'en' in m['locales']:
            return dict(title=m['locales']['en']['title'],lang='en',note='',href=f"writing/{a['slug']}-en.html")
        if english:return dict(title=english['title'],lang='en',note='in Japanese',href=f"writing/{a['slug']}.html")
        return dict(title=m['locales'][m['source_language']]['title'],lang=m['source_language'],note='in Japanese' if m['source_language']=='ja' else '',href=f"writing/{a['slug']}.html")
    published={a['slug']:profile_link(a) for a in entries}
    def cite_text(m,title,file):
        english=m['locales'].get('en') or m.get('english')
        citation_title=english['title'] if english else title
        citation_title=citation_title.rstrip('. ')
        language_note=' [Article in Japanese]' if 'en' not in m['locales'] else ''
        if 'en' in m['locales']:
            file=file.removesuffix('-ja.html').removesuffix('-en.html').removesuffix('.html')+('' if m['source_language']=='en' else '-en')+'.html'
        punctuation='' if not language_note and citation_title.endswith(('?', '!')) else '.'
        return f"Kumakura, D. ({m['date'][:4]}). {citation_title}{language_note}{punctuation} daikikumakura.github.io. {SITE_URL}writing/{file}"
    def glossary_terms(slug,language):
        """Glossary pages that list this article as related, in the article's language."""
        found=[]
        for e in reference:
            if e['kind']=='term' and slug in e['meta'].get('related_articles',[]):
                found.append(dict(title=e['meta']['locales'][language]['title'],href='../'+reference_file(e,language),url=SITE_URL+reference_file(e,language)))
        return found
    def output(name,page,lang='en',article=None,og_image=None,topics=None,terms=None):
        canonical=SITE_URL if name in ('index.html','home.html') else SITE_URL+name
        page=enrich(page,name,site,SITE_URL,article,og_image,topics,terms)
        page=page.replace('</head>',f'<link rel="canonical" href="{canonical}">\n</head>')
        outputs[name]=page.encode('utf-8')
    for key,title in NAV.items():
        page=env.get_template('page.html').render(site=site,lang='en',ui=ui,preview=preview,active=key,root='',title=site['name'] if key=='home' else title,description=site['profile'],math=False,articles=listings_en if key in ('home','writing') else listings,recent=listings_en[:RECENT_ON_HOME],working_papers=[a for a in listings if a['category']=='paper'],alternatives=WRITING_ALTERNATIVES if key=='writing' else {},lead=WRITING_LEAD['en'] if key=='writing' else '')
        output(key+'.html',page)
        if key=='home':outputs['index.html']=outputs['home.html']
    page=env.get_template('page.html').render(site=site,lang='ja',ui=ui,preview=preview,active='writing',root='',title=WRITING_TITLE_JA,description=WRITING_DESCRIPTION_JA,math=False,articles=listings_ja,recent=[],working_papers=[],alternatives=WRITING_ALTERNATIVES,lead=WRITING_LEAD['ja'])
    output('writing-ja.html',page,'ja')
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
            page=env.get_template('article.html').render(site=site,lang=language,ui=ui,preview=preview,active='writing',root='../',alternatives=alternatives,title=m['locales'][language]['title'],description=m['locales'][language]['summary'],math=m.get('math',False),author=m.get('author',site['name']),date=m['date'],category=m['category'],version=m.get('version',''),draft=m['draft'],stale=a['stale'][language],body=body,toc=toc,has_abstract=bool(re.search(r'<h2[^>]*>(?:要旨|Abstract)</h2>',body)),key_findings=m['locales'][language].get('key_findings',[]),english=m.get('english') if language!='en' and 'en' not in m['locales'] else None,cite=cite_text(m,m['locales'][language]['title'],alternatives[language]),terms=glossary_terms(a['slug'],language))
            output('writing/'+alternatives[language],page,language,m,og_card,terms=glossary_terms(a['slug'],language))
        for asset in (a['folder']/'shared').rglob('*'):
            if asset.is_file():outputs[f"writing/shared/{a['slug']}/{asset.relative_to(a['folder']/'shared').as_posix()}"]=asset.read_bytes()
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
    canonical_pages=['index.html']+[key+'.html' for key in NAV if key!='home']+['writing-ja.html']+[name for name in outputs if name.startswith(('writing/','topics/','software/','about/','tools/','glossary/','catalog/','reference.html')) and name.endswith('.html')]
    if not preview:
        redirects=dict(LEGACY_REDIRECTS)
        redirects.update({path:'writing.html' for path in site.get('legacy_topic_paths',[])})
        redirects.update({f'topics/cluster-{number}.html':'writing.html' for number in range(1,11) if f'topics/cluster-{number}.html' not in outputs})
        for old,new in redirects.items():
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
        lastmod['index.html']=lastmod['writing.html']=lastmod['writing-ja.html']=newest
    for e in reference:
        for code in ('en','ja'):lastmod[reference_file(e,code)]=e['meta']['updated']
    if reference:lastmod['reference.html']=max(e['meta']['updated'] for e in reference)
    def sitemap_url(p):
        tag='<url><loc>'+html.escape(SITE_URL if p=='index.html' else SITE_URL+p)+'</loc>'
        if p in lastmod:tag+='<lastmod>'+lastmod[p]+'</lastmod>'
        if p.startswith('writing/') and p in outputs:
            # Figures of the article, so that they can appear in image search (relative to the article's folder).
            for src in dict.fromkeys(re.findall(r'<img[^>]+src="(shared/[^"]+\.(?:png|jpe?g))"',outputs[p].decode('utf-8'))):
                tag+='<image:image><image:loc>'+html.escape(SITE_URL+'writing/'+src)+'</image:loc></image:image>'
        if p in WRITING_ALTERNATIVES.values():
            tag+=''.join('<xhtml:link rel="alternate" hreflang="'+code+'" href="'+html.escape(SITE_URL+name)+'"/>' for code,name in WRITING_ALTERNATIVES.items())+'<xhtml:link rel="alternate" hreflang="x-default" href="'+html.escape(SITE_URL+WRITING_ALTERNATIVES['en'])+'"/>'
        for a in entries:
            m=a['meta']; files={code:'writing/'+a['slug']+('' if code==m['source_language'] else '-'+code)+'.html' for code in m['locales']}
            if p not in files.values() or len(files)<2:continue
            for code,name in files.items():tag+='<xhtml:link rel="alternate" hreflang="'+code+'" href="'+html.escape(SITE_URL+name)+'"/>'
            if 'en' in files:tag+='<xhtml:link rel="alternate" hreflang="x-default" href="'+html.escape(SITE_URL+files['en'])+'"/>'
        return tag+'</url>'
    outputs['sitemap.xml']=('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'+''.join(sitemap_url(p) for p in canonical_pages if not preview or not p.startswith('writing/'))+'</urlset>').encode('utf-8')
    if not preview:
        outputs['feed.xml']=atom_feed(site,entries)
        for code in ('en','ja'):outputs[f'feed-{code}.xml']=atom_feed(site,entries,code)
    outputs['robots.txt']=('User-agent: *\n'+('Disallow: /\n' if preview else 'Allow: /\nSitemap: '+SITE_URL+'sitemap.xml\nSitemap: '+SITE_URL+'feed.xml\nSitemap: '+SITE_URL+'feed-en.xml\nSitemap: '+SITE_URL+'feed-ja.xml\n'+''.join('Sitemap: '+SITE_URL+path+'\n' for path in EXTRA_SITEMAPS))).encode('utf-8')
    if not preview:
        outputs['llms.txt']=llms_txt(site,entries,reference=reference)
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

def llms_txt(site, entries, reference=()):
    """Plain-text site guide (llmstxt.org format) for language models and agents.

    It restates the third-person summary, the identities that belong to the same person,
    and every live article with its key findings."""
    names = ', '.join(site.get('alternate_names', [site['alternate_name']]))
    lines = ['# ' + site['name'] + ' (' + site['alternate_name'] + ')', '', '> ' + site.get('bio', site['profile']), '',
             'Also written as: ' + names + '. All analyses use public data or simulation only and are not clinical or regulatory work.', '',
             '## Identity', '',
             f"- ORCID: {site['orcid']}", f"- Google Scholar: {site['scholar']}", f"- GitHub: {site['github']}", f"- Qiita: {site['qiita']}", f"- LinkedIn: {site['linkedin']}", '',
             '## Pages', '']
    for key, label in NAV.items():
        page = SITE_URL if key == 'home' else SITE_URL + key + '.html'
        lines.append(f'- [{label}]({page})')
        if key == 'writing':
            lines.append(f'- [記事一覧（日本語）]({SITE_URL}writing-ja.html)')
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

def feed_entry_text(meta, language):
    """Title, summary, language and file of an article for one feed language (None: the original).

    An article without a version in that language is listed in its original language, using the
    English summary of a Japanese original in the English feed."""
    original = meta['source_language']
    if language is None or language == original:
        return meta['locales'][original], original, ''
    if language in meta['locales']:
        return meta['locales'][language], language, '-' + language
    if language == 'en' and meta.get('english'):
        return meta['english'], 'en', ''
    return meta['locales'][original], original, ''

def atom_feed(site, entries, language=None):
    """Atom feed of published articles (also accepted by search engines as a sitemap).

    Without a language the entries keep the language of the original (feed.xml). With 'en' or 'ja'
    every title and summary is in that language where the article has it (feed-en.xml, feed-ja.xml)."""
    name = 'feed.xml' if language is None else f'feed-{language}.xml'
    index = 'writing.html' if language in (None, 'en') else 'writing-ja.html'
    label = {None: 'Writing', 'en': 'Writing (English)', 'ja': '記事（日本語）'}[language]
    items=[]
    for a in entries[:FEED_SIZE]:
        m=a['meta']; loc, lang, suffix = feed_entry_text(m, language)
        url=SITE_URL+'writing/'+a['slug']+suffix+'.html'
        published=datetime.fromisoformat(m['publish_at']).isoformat() if m.get('publish_at') else m['date']+'T00:00:00+09:00'
        items.append('<entry><title>'+html.escape(loc['title'])+'</title><link rel="alternate" type="text/html" href="'+url+'"/><id>'+url+'</id>'
                     '<published>'+published+'</published><updated>'+atom_time(m)+'</updated><summary xml:lang="'+lang+'">'+html.escape(loc['summary'])+'</summary></entry>')
    updated=max((atom_time(a['meta']) for a in entries),default='2026-01-01T00:00:00+09:00')
    head=('<?xml version="1.0" encoding="UTF-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom"'+(f' xml:lang="{language}"' if language else '')+'><title>'+html.escape(label)+' | '+html.escape(site['name'])+'</title>'
          '<link rel="self" type="application/atom+xml" href="'+SITE_URL+name+'"/><link rel="alternate" type="text/html" href="'+SITE_URL+index+'"/>'
          '<id>'+SITE_URL+name+'</id><updated>'+updated+'</updated><author><name>'+html.escape(site['name'])+'</name><uri>'+SITE_URL+'</uri></author>')
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

