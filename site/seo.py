"""Public search metadata; never infer professional claims from keywords."""
import html
import json
import re
from urllib.parse import urljoin

DESCRIPTIONS = {
 'home': 'Daiki Kumakura (熊倉大騎), mathematical biologist and bioinformatics researcher. PK/PD and dosing analyses of public data, research software and publications.',
 'profile': 'Profile of Daiki Kumakura: mathematical modeling and statistical inference, with public-data analyses of population PK, PK/PD, exposure–response and dosing.',
 'writing': 'Analysis tutorials, technical notes, blog posts and working papers by Daiki Kumakura. Each article is available in its original language.',
 'software': 'Research software by Daiki Kumakura: pkident for PK/PD identifiability, rsemflow for RNA-seq downstream analysis, retiaudit, RLR_transform and CRiSM.',
 'publication': 'Research publications by Daiki Kumakura: mathematical models, biological dynamics, antibiotic response, compositional time series and bioinformatics.',
 'activity': 'Conference presentations, teaching, event organization, outreach and media activities by Daiki Kumakura, grouped by year and category.'}

HOME_TITLE='Daiki Kumakura / 熊倉大騎 — PK/PD and Mathematical Biology'  # 58 cells: not cut in search results

DEFAULT_IMAGE='assets/og-default.png'
IMAGE_SIZE=(1200,630)
DEFAULT_IMAGE_ALT='Daiki Kumakura: mathematical biology and PK/PD modeling'

def first_raster(page, base):
 """First PNG/JPEG figure in the page: (absolute url, width, height, alt) or None."""
 for tag in re.findall(r'<img\b[^>]*>',page):
  src=re.search(r'\ssrc="([^"]+)"',tag)
  if not src or not html.unescape(src[1]).lower().endswith(('.png','.jpg','.jpeg')):continue
  size=[re.search(rf'\s{k}="(\d+)"',tag) for k in ('width','height')]
  alt=re.search(r'\salt="([^"]*)"',tag)
  return (urljoin(base,html.unescape(src[1])),int(size[0][1]) if size[0] else None,int(size[1][1]) if size[1] else None,html.unescape(alt[1]) if alt else '')
 return None

def enrich(page, name, site, site_url, article=None, og_image=None, topics=None, terms=None):
 """article is the article's meta.json, used for dates, the English summary and the
 optional per-locale seo_title / seo_description. og_image is the published path of
 the article's 1200x630 card (relative to the site root), if it has one."""
 key=name.removesuffix('.html'); home=key in ('index','home')
 canonical=site_url if home else site_url+name
 lang=re.search(r'<html lang="([^"]+)"',page); lang=lang[1] if lang else 'en'
 title=html.unescape(re.search(r'<title>(.*?)</title>',page)[1])
 headline=title.removesuffix(' | '+site['name'])
 description=DESCRIPTIONS.get('home' if home else key)
 if description is None:description=html.unescape(re.search(r'<meta name="description" content="([^"]*)">',page)[1])
 locale=(article or {}).get('locales',{}).get(lang,{})
 # Search-result text may be shorter than the article's own title and summary;
 # the heading, the structured-data headline and the page itself keep the full text.
 if locale.get('seo_title'):title=locale['seo_title']
 if locale.get('seo_description'):description=locale['seo_description']
 if home:title=HOME_TITLE
 page=re.sub(r'<title>.*?</title>',lambda _: '<title>'+html.escape(title)+'</title>',page)
 page=re.sub(r'\s*<meta name="description" content="[^"]*">','',page)
 page=re.sub(r'(<link rel="alternate" hreflang="[^"]+" href=")([^"]+)',lambda m:m[1]+urljoin(canonical,m[2]),page)
 metadata=['<meta name="description" content="'+html.escape(description,quote=True)+'">']
 for prop,value in {'og:type':'article' if name.startswith('writing/') else 'website','og:title':title,'og:description':description,'og:url':canonical,'og:site_name':site['name'],'og:locale':'ja_JP' if lang=='ja' else 'en_US'}.items():
  metadata.append(f'<meta property="{prop}" content="{html.escape(value,quote=True)}">')
 image=None
 if og_image:image=(site_url+og_image,)+IMAGE_SIZE+(headline,)
 elif name.startswith('writing/'):image=first_raster(page,canonical)
 if image is None:image=(site_url+DEFAULT_IMAGE,)+IMAGE_SIZE+(DEFAULT_IMAGE_ALT,)
 metadata.append('<meta property="og:image" content="'+html.escape(image[0],quote=True)+'">')
 if image[1] and image[2]:
  metadata.append(f'<meta property="og:image:width" content="{image[1]}">');metadata.append(f'<meta property="og:image:height" content="{image[2]}">')
 metadata.append('<meta property="og:image:alt" content="'+html.escape(image[3] or headline,quote=True)+'">')
 metadata.append('<meta name="twitter:card" content="summary_large_image">')
 person={'@type':'Person','@id':site_url+'#person','name':site['name'],'alternateName':site.get('alternate_names',[site['alternate_name']]),'url':site_url+'profile.html','description':site.get('bio',site['profile']),'knowsLanguage':['ja','en'],'identifier':{'@type':'PropertyValue','propertyID':'ORCID','value':site['orcid'].rsplit('/',1)[-1],'url':site['orcid']},'jobTitle':'Bioinformatics Researcher','knowsAbout':['Mathematical biology','Mathematical modeling','Bioinformatics','Pharmacometrics','Model-informed drug development','Population pharmacokinetics','PK/PD modeling','Exposure–response analysis','Systems biology','Statistical inference','Time-series analysis'],'alumniOf':{'@type':'CollegeOrUniversity','name':'Hokkaido University','sameAs':'https://www.global.hokudai.ac.jp/'},'sameAs':[site['github'],site['qiita'],site['docker'],site['orcid'],site['scholar'],site['linkedin']]}
 schema=None
 if name.startswith('writing/') and name.endswith('.html'):
  schema={'@context':'https://schema.org','@type':'Article','@id':canonical+'#article','url':canonical,'headline':headline,'description':description,'inLanguage':lang,'isAccessibleForFree':True,'author':person,'publisher':{'@id':site_url+'#person'},'isPartOf':{'@type':'WebSite','@id':site_url+'#website','url':site_url},'mainEntityOfPage':canonical}
  if topics:schema['keywords']=topics;schema['articleSection']=topics[0]
  published=re.search(r'<p class="meta">[^<]*?(\d{4}-\d{2}-\d{2})',page)
  if published:schema['datePublished']=published[1]
  citations=list(dict.fromkeys(html.unescape(url) for url in re.findall(r'href="(https://doi\.org/[^"]+)"',page)))
  if citations:schema['citation']=citations
  images=[urljoin(canonical,html.unescape(url)) for url in re.findall(r'<img[^>]+src="([^"]+)"',page)]
  if og_image:images.insert(0,site_url+og_image)
  if images:schema['image']=images
  if article:
   schema['datePublished']=article['date'];schema['dateModified']=article.get('updated') or article['date']
   if article.get('english'):schema['alternativeHeadline']=article['english']['title'];schema['abstract']=article['english']['summary']
  hreflangs=dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"',page))
  if article:
   source=article.get('source_language')
   if source in hreflangs and source!=lang:schema['translationOfWork']={'@type':'Article','@id':hreflangs[source]+'#article','url':hreflangs[source],'inLanguage':source}
   translated=[{'@type':'Article','@id':url+'#article','url':url,'inLanguage':code} for code,url in hreflangs.items() if code!=lang]
   if translated and source==lang:schema['workTranslation']=translated
  if {'ja','en'}<=set(hreflangs):metadata.append('<link rel="alternate" hreflang="x-default" href="'+html.escape(hreflangs['en'],quote=True)+'">')
  metadata.append('<meta name="author" content="'+html.escape(site['name'],quote=True)+'">')
  if terms:schema['mentions']=[{'@type':'DefinedTerm','name':t['title'],'url':t['url']} for t in terms]
  if article:
   # Reference managers (Zotero, Mendeley) and Google Scholar read the citation_* tags; the DC.* tags are the Dublin Core equivalents.
   given,_,family=site['name'].rpartition(' ')
   scholarly=[('citation_title',headline),('citation_author',family+', '+given),('citation_publication_date',article['date'].replace('-','/')),('citation_online_date',article['date'].replace('-','/')),('citation_language',lang),('citation_abstract_html_url',canonical),
              ('DC.title',headline),('DC.creator',site['name']),('DC.date',article['date']),('DC.language',lang),('DC.identifier',canonical)]
   scholarly+=[('citation_reference','citation_doi='+doi.removeprefix('https://doi.org/')) for doi in citations]
   metadata+=['<meta name="'+n+'" content="'+html.escape(v,quote=True)+'">' for n,v in scholarly]
   metadata.append('<meta property="article:published_time" content="'+article['date']+'">')
   metadata.append('<meta property="article:modified_time" content="'+(article.get('updated') or article['date'])+'">')
 elif home:
  schema={'@context':'https://schema.org','@type':'WebSite','@id':site_url+'#website','url':site_url,'name':site['name'],'alternateName':site['alternate_name'],'inLanguage':'en','about':person}
 elif key=='profile':
  schema={'@context':'https://schema.org','@type':'ProfilePage','url':canonical,'inLanguage':'en','mainEntity':person}
 elif key=='publication':
  works=[{'@type':'ListItem','position':i+1,'item':{'@type':'Thesis' if p['kind']=='thesis' else 'ScholarlyArticle','name':p.get('title_translation',p['title']),'url':'https://doi.org/'+p['doi'],'identifier':{'@type':'PropertyValue','propertyID':'DOI','value':p['doi']},'datePublished':str(p['year']),'isPartOf':{'@type':'Periodical' if p['kind']!='thesis' else 'CreativeWork','name':p['venue']},'author':[{'@type':'Person','name':a['name']} for a in p['author_list']]}} for i,p in enumerate(sorted(site['publications'],key=lambda p:p['year'],reverse=True))]
  schema={'@context':'https://schema.org','@type':'CollectionPage','url':canonical,'name':'Publication | '+site['name'],'mainEntity':{'@type':'ItemList','itemListElement':works}}
 elif key=='software':
  works=[{'@type':'ListItem','position':i+1,'item':{'@type':'SoftwareSourceCode','name':s['id'],'description':s['description'],'codeRepository':s['url'],'programmingLanguage':s['tech'],'author':{'@id':site_url+'#person'}}} for i,s in enumerate(site['software'])]
  schema={'@context':'https://schema.org','@type':'CollectionPage','url':canonical,'name':'Software | '+site['name'],'about':person,'mainEntity':{'@type':'ItemList','itemListElement':works}}
 elif name.startswith('topics/'):
  schema={'@context':'https://schema.org','@type':'CollectionPage','url':canonical,'name':headline,'description':description,'inLanguage':'en','about':person,'isPartOf':{'@type':'WebSite','@id':site_url+'#website','url':site_url}}
 elif name.startswith('software/'):
  sw=next((x for x in site['software'] if x.get('slug')==key.split('/',1)[1]),None)
  if sw:schema={'@context':'https://schema.org','@type':'SoftwareSourceCode','@id':canonical+'#software','url':canonical,'name':sw['id'],'description':sw['summary'],'codeRepository':sw['url'],'programmingLanguage':sw['tech'],'author':person,'isAccessibleForFree':True}
 elif name.startswith(('tools/','glossary/','catalog/')):
  entry=article or {}
  hub=site_url+'reference.html'
  base={'@context':'https://schema.org','url':canonical,'inLanguage':lang,'isAccessibleForFree':True,'author':person,'dateModified':entry.get('updated'),'isPartOf':{'@type':'WebSite','@id':site_url+'#website','url':site_url}}
  if name.startswith('tools/'):
   schema=dict(base,**{'@type':'WebApplication','name':headline,'description':description,'applicationCategory':'ScientificApplication','operatingSystem':'Any (web browser)','browserRequirements':'JavaScript','offers':{'@type':'Offer','price':'0','priceCurrency':'USD'}})
  elif name.startswith('glossary/'):
   schema=dict(base,**{'@type':'DefinedTerm','name':headline,'description':description,'inDefinedTermSet':{'@type':'DefinedTermSet','name':'Pharmacometrics terms | '+site['name'],'url':site_url+'reference.html#glossary'}})
  else:
   schema=dict(base,**{'@type':'CollectionPage','name':headline,'description':description,'about':person})
  hreflangs=dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"',page))
  if {'ja','en'}<=set(hreflangs):metadata.append('<link rel="alternate" hreflang="x-default" href="'+html.escape(hreflangs['en'],quote=True)+'">')
  faq=[(h,a) for h,a in re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>',page.split('data-faq',1)[1],flags=re.S)] if 'data-faq' in page else []
  if faq:
   questions={'@context':'https://schema.org','@type':'FAQPage','inLanguage':lang,'mainEntity':[{'@type':'Question','name':html.unescape(q),'acceptedAnswer':{'@type':'Answer','text':html.unescape(re.sub(r'<[^>]+>','',a))}} for q,a in faq]}
   metadata.append('<script type="application/ld+json">'+json.dumps(questions,ensure_ascii=False).replace('<','\\u003c')+'</script>')
  schema={k:v for k,v in schema.items() if v is not None}
 elif key in ('writing','writing-ja','activity','reference'):
  schema={'@context':'https://schema.org','@type':'CollectionPage','url':canonical,'name':title,'about':person}
  if key in ('writing','writing-ja'):
   schema['inLanguage']=lang
   hreflangs=dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"',page))
   if {'ja','en'}<=set(hreflangs):metadata.append('<link rel="alternate" hreflang="x-default" href="'+html.escape(hreflangs['en'],quote=True)+'">')
 if schema:metadata.append('<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script>')
 if name.startswith('writing/') and name.endswith('.html'):
  crumbs={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':site_url},{'@type':'ListItem','position':2,'name':'Writing','item':site_url+'writing.html'},{'@type':'ListItem','position':3,'name':headline,'item':canonical}]}
  metadata.append('<script type="application/ld+json">'+json.dumps(crumbs,ensure_ascii=False).replace('<','\\u003c')+'</script>')
 if name.startswith('topics/'):
  crumbs={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':site_url},{'@type':'ListItem','position':2,'name':'Writing','item':site_url+'writing.html'},{'@type':'ListItem','position':3,'name':headline,'item':canonical}]}
  metadata.append('<script type="application/ld+json">'+json.dumps(crumbs,ensure_ascii=False).replace('<','\\u003c')+'</script>')
 if name.startswith(('tools/','glossary/','catalog/')) and schema:
  crumbs={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':site_url},{'@type':'ListItem','position':2,'name':'Tools and reference','item':site_url+'reference.html'},{'@type':'ListItem','position':3,'name':headline,'item':canonical}]}
  metadata.append('<script type="application/ld+json">'+json.dumps(crumbs,ensure_ascii=False).replace('<','\\u003c')+'</script>')
 if name.startswith('software/') and schema:
  crumbs={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':site_url},{'@type':'ListItem','position':2,'name':'Software','item':site_url+'software.html'},{'@type':'ListItem','position':3,'name':schema['name'],'item':canonical}]}
  metadata.append('<script type="application/ld+json">'+json.dumps(crumbs,ensure_ascii=False).replace('<','\\u003c')+'</script>')
 return page.replace('</head>','\n'.join(metadata)+'\n</head>')


