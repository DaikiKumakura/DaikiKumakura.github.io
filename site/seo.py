"""Public search metadata; never infer professional claims from keywords."""
import html
import json
import re
from urllib.parse import urljoin

DESCRIPTIONS = {
 'home': 'Daiki Kumakura (熊倉大騎), mathematical biologist and bioinformatics researcher. PK/PD and dosing analyses of public data, research software and publications.',
 'profile': 'Profile of Daiki Kumakura: mathematical modeling, statistical inference and dynamic systems; pharmacometrics and model-informed drug development.',
 'writing': 'Analysis tutorials, technical notes, blog posts and working papers by Daiki Kumakura. Each article is available in its original language.',
 'software': 'Research software by Daiki Kumakura: RLR_transform for CCM (Convergent Cross Mapping), CRiSM, shotgun metagenomics tutorials and Docker environments.',
 'publication': 'Research publications by Daiki Kumakura: mathematical models, biological dynamics, antibiotic response, compositional time series and bioinformatics.',
 'activity': 'Conference presentations, teaching, event organization, outreach and media activities by Daiki Kumakura, grouped by year and category.'}

HOME_TITLE='Daiki Kumakura / 熊倉大騎 — Mathematical Biology and PK/PD Modeling'

def enrich(page, name, site, site_url):
 key=name.removesuffix('.html'); home=key in ('index','home')
 canonical=site_url if home else site_url+name
 lang=re.search(r'<html lang="([^"]+)"',page); lang=lang[1] if lang else 'en'
 title=html.unescape(re.search(r'<title>(.*?)</title>',page)[1])
 description=DESCRIPTIONS.get('home' if home else key)
 if description is None:description=html.unescape(re.search(r'<meta name="description" content="([^"]*)">',page)[1])
 if home:title=HOME_TITLE
 page=re.sub(r'<title>.*?</title>',lambda _: '<title>'+html.escape(title)+'</title>',page)
 page=re.sub(r'\s*<meta name="description" content="[^"]*">','',page)
 page=re.sub(r'(<link rel="alternate" hreflang="[^"]+" href=")([^"]+)',lambda m:m[1]+urljoin(canonical,m[2]),page)
 metadata=['<meta name="description" content="'+html.escape(description,quote=True)+'">']
 for prop,value in {'og:type':'article' if name.startswith('writing/') else 'website','og:title':title,'og:description':description,'og:url':canonical,'og:site_name':site['name'],'og:locale':'ja_JP' if lang=='ja' else 'en_US'}.items():
  metadata.append(f'<meta property="{prop}" content="{html.escape(value,quote=True)}">')
 metadata.append('<meta name="twitter:card" content="summary">')
 person={'@type':'Person','@id':site_url+'#person','name':site['name'],'alternateName':site['alternate_name'],'url':site_url+'profile.html','description':site['profile'],'jobTitle':'Bioinformatics Researcher','knowsAbout':['Mathematical biology','Mathematical modeling','Bioinformatics','Pharmacometrics','Model-informed drug development','Systems biology','Statistical inference','Time-series analysis'],'alumniOf':{'@type':'CollegeOrUniversity','name':'Hokkaido University','sameAs':'https://www.global.hokudai.ac.jp/'},'sameAs':[site['github'],site['qiita'],site['docker'],site['orcid'],site['linkedin']]}
 schema=None
 if name.startswith('writing/') and name.endswith('.html'):
  schema={'@context':'https://schema.org','@type':'Article','@id':canonical+'#article','url':canonical,'headline':title.removesuffix(' | '+site['name']),'description':description,'inLanguage':lang,'author':person,'mainEntityOfPage':canonical}
  published=re.search(r'<p class="meta">[^<]*?(\d{4}-\d{2}-\d{2})',page)
  if published:schema['datePublished']=published[1]
  citations=list(dict.fromkeys(html.unescape(url) for url in re.findall(r'href="(https://doi\.org/[^"]+)"',page)))
  if citations:schema['citation']=citations
  images=re.findall(r'<img[^>]+src="([^"]+)"',page)
  if images:schema['image']=[urljoin(canonical,html.unescape(url)) for url in images]
 elif home:
  schema={'@context':'https://schema.org','@type':'WebSite','@id':site_url+'#website','url':site_url,'name':site['name'],'alternateName':site['alternate_name'],'inLanguage':'en','about':person}
 elif key=='profile':
  schema={'@context':'https://schema.org','@type':'ProfilePage','url':canonical,'inLanguage':'en','mainEntity':person}
 elif key=='publication':
  works=[{'@type':'ListItem','position':i+1,'item':{'@type':'CreativeWork','name':p.get('title_translation',p['title']),'url':'https://doi.org/'+p['doi'],'author':[{'@type':'Person','name':a['name']} for a in p['author_list']]}} for i,p in enumerate(sorted(site['publications'],key=lambda p:p['year'],reverse=True))]
  schema={'@context':'https://schema.org','@type':'CollectionPage','url':canonical,'name':'Publication | '+site['name'],'mainEntity':{'@type':'ItemList','itemListElement':works}}
 elif key=='software':
  works=[{'@type':'ListItem','position':i+1,'item':{'@type':'SoftwareSourceCode','name':s['id'],'description':s['description'],'codeRepository':s['url'],'programmingLanguage':s['tech'],'author':{'@id':site_url+'#person'}}} for i,s in enumerate(site['software'])]
  schema={'@context':'https://schema.org','@type':'CollectionPage','url':canonical,'name':'Software | '+site['name'],'about':person,'mainEntity':{'@type':'ItemList','itemListElement':works}}
 elif key in ('writing','activity'):
  schema={'@context':'https://schema.org','@type':'CollectionPage','url':canonical,'name':title,'about':person}
 if schema:metadata.append('<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script>')
 return page.replace('</head>','\n'.join(metadata)+'\n</head>')


