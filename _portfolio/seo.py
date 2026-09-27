"""Search and sharing metadata from the same public profile as the pages."""
import html
import json
import re

DESCRIPTIONS = {
    'ja': {
        'index': '熊倉大騎（Daiki Kumakura）の個人サイト。数理生物学を専門とする、製薬企業のバイオインフォマティクス研究者。論文、研究コード、解析記事、活動記録を掲載。',
        'about': '熊倉大騎（Daiki Kumakura）のプロフィール。博士（生命科学）、北海道大学。数理生物学、微生物の増殖・薬剤応答、時系列解析の研究背景と経歴。',
        'publications': '熊倉大騎（Daiki Kumakura）の研究業績。微生物増殖の数理モデル、抗菌薬応答、微生物叢の時系列解析などの論文・学位論文と出典。',
        'software': '熊倉大騎の研究コードとソフトウェア。RLR_transform、CRiSM、ショットガンメタゲノム解析教材、Dockerfileの概要とGitHubへのリンク。',
        'writing': '熊倉大騎の解析記事・技術メモ・ブログ・未査読の論考の掲載ページ。公開済みの記事と利用できる言語を案内。',
        'activities': '熊倉大騎の学会発表、研究会、教育、企画、メディア関連の活動記録。過去の活動を年別・種類別に掲載。',
    },
    'en': {
        'index': 'Daiki Kumakura is a mathematical biologist and bioinformatics researcher in the pharmaceutical industry. Publications, research software, analysis articles and activities.',
        'about': 'Profile of Daiki Kumakura, Ph.D. in Life Science from Hokkaido University. Research background in mathematical biology, microbial growth, antibiotic response and time-series analysis.',
        'publications': 'Publications by Daiki Kumakura on mathematical models of microbial growth, antibiotic response and microbial community time series, with source links and doctoral thesis.',
        'software': 'Research software by Daiki Kumakura: RLR_transform, CRiSM, shotgun metagenomics tutorials and Dockerfiles, with descriptions and GitHub repositories.',
        'writing': 'Analysis tutorials, technical notes, blog posts and working papers by Daiki Kumakura. Browse published articles and available languages.',
        'activities': 'Conference presentations, teaching, event organization and media activities by Daiki Kumakura, organized by year and category.',
    },
}

def enrich(page, name, site, site_url):
    canonical = site_url if name == 'index.html' else site_url + name
    parts = name.split('/')
    lang = parts[0] if parts[0] in ('ja', 'en') else 'en'
    key = parts[-1].removesuffix('.html')
    root = name == 'index.html'
    title = re.search(r'<title>(.*?)</title>', page).group(1)
    if root:
        title = 'Daiki Kumakura / 熊倉大騎 — Mathematical Biology'
        description = DESCRIPTIONS['en']['index']
    elif len(parts) == 2:
        label = '熊倉大騎 / Daiki Kumakura' if lang == 'ja' else site['name']
        title = label + (' — 数理生物学・バイオインフォマティクス' if lang == 'ja' else ' — Mathematical Biology & Bioinformatics') if key == 'index' else html.unescape(title).replace(site['name'], label)
        description = DESCRIPTIONS[lang][key]
    else:
        description = html.unescape(re.search(r'<meta name="description" content="([^"]*)">', page).group(1))
        title = html.unescape(title)
    page = re.sub(r'<title>.*?</title>', lambda _: '<title>'+html.escape(title)+'</title>', page)
    page = re.sub(r'\s*<meta name="description" content="[^"]*">', '', page)
    metadata = ['<meta name="description" content="'+html.escape(description, quote=True)+'">']
    for prop, value in {'og:type':'website', 'og:title':title, 'og:description':description, 'og:url':canonical, 'og:site_name':site['name'], 'og:locale':'ja_JP' if lang == 'ja' else 'en_US'}.items():
        metadata.append(f'<meta property="{prop}" content="{html.escape(value, quote=True)}">')
    metadata.append('<meta name="twitter:card" content="summary">')
    if root:
        for code, path in [('ja','ja/index.html'),('en','en/index.html'),('x-default','')]:
            metadata.append(f'<link rel="alternate" hreflang="{code}" href="{site_url+path}">')
    elif len(parts) == 2 and key == 'index':
        metadata.append(f'<link rel="alternate" hreflang="x-default" href="{site_url}">')
    schema = None
    if root:
        schema = {'@context':'https://schema.org','@type':'WebSite','@id':site_url+'#website','url':site_url,'name':site['name'],'alternateName':'熊倉大騎','inLanguage':['ja','en']}
    elif len(parts) == 2 and key == 'about':
        schema = {'@context':'https://schema.org','@type':'ProfilePage','url':canonical,'inLanguage':lang,'mainEntity':{'@type':'Person','@id':site_url+'#person','name':site['name'],'alternateName':'熊倉大騎','url':site_url,'description':site['profile'][lang],'sameAs':[site['github'],site['orcid'],site['linkedin']]}}
    if schema:
        metadata.append('<script type="application/ld+json">'+json.dumps(schema, ensure_ascii=False).replace('<','\\u003c')+'</script>')
    return page.replace('</head>', '\n'.join(metadata)+'\n</head>')
