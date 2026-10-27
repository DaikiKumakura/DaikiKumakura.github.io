import json
import re
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import build

class Links(HTMLParser):
 def __init__(self):
  super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  for k in ('href','src'):
   if k in a:self.links.append(a[k])

class BuildTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
  # Test fixtures must not collide with or depend on real articles and drafts.
  for n in ('content','templates','assets','static'):
   shutil.copytree(build.BASE/n,self.root/n,ignore=shutil.ignore_patterns('articles','reference') if n=='content' else None)
  shutil.copytree(build.BASE/'fixtures/articles',self.root/'content/articles',dirs_exist_ok=True)
 def tearDown(self):self.temp.cleanup()
 def text(self,name):return (self.root/'dist'/name).read_text(encoding='utf-8')
 def meta(self,slug):
  p=self.root/'content/articles'/slug/'meta.json';return p,build.read_json(p)
 def test_scheduled_article_boundary(self):
  from datetime import datetime
  p,m=self.meta('japanese-note');m.update(draft=False,date='2026-10-04',publish_at='2026-10-04T09:00:00+09:00');p.write_text(json.dumps(m),encoding='utf-8')
  before=datetime.fromisoformat('2026-10-03T23:59:59+00:00')
  after=datetime.fromisoformat('2026-10-04T00:00:00+00:00')
  self.assertNotIn('japanese-note',[a['slug'] for a in build.load_articles(self.root/'content',now=before)])
  self.assertIn('japanese-note',[a['slug'] for a in build.load_articles(self.root/'content',now=after)])
  self.assertIn('japanese-note',[a['slug'] for a in build.load_articles(self.root/'content',preview=True,now=before)])
 def test_scheduled_article_requires_timezone(self):
  p,m=self.meta('japanese-note');m['publish_at']='2026-10-04T09:00:00';p.write_text(json.dumps(m),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'timezone'):build.load_articles(self.root/'content')
 def test_preserves_records(self):
  site=build.read_json(self.root/'content/site.json');build.build(self.root)
  self.assertEqual(len(site['publications']),10);self.assertEqual(len(site['activities']),70)
  for a in site['activities']:self.assertIn('activity-'+a['id'],self.text('activity.html'))
  for p in site['publications']:self.assertIn(p['doi'],self.text('publication.html'))
 def test_home_profile_and_navigation(self):
  build.build(self.root);home=self.text('index.html')
  self.assertEqual(home,self.text('home.html'))
  self.assertNotIn('id="growth-2023"',home);self.assertNotIn('software-RLR',home)
  self.assertIn('favicon.svg',home);self.assertIn('msvalidate.01',home)
  self.assertIn('alt="Data processing and quantitative modeling illustration"',home)
  self.assertNotIn('aria-hidden="true"',home)
  profile=self.text('profile.html')
  self.assertNotIn('Best Award',profile);self.assertNotIn('Functional Specialization',profile)
  self.assertIn('Bachelor’s degree in Fisheries Science, Department of Aquaculture Life Science, School of Fisheries Sciences, Hokkaido University',profile)
  self.assertNotIn('Aquaculture and Life Science',profile);self.assertNotIn('Faculty of Fisheries Sciences',profile)
  positions=[home.index('>'+label+'</a>') for label in build.NAV.values()]
  self.assertEqual(positions,sorted(positions))
 def test_legacy_redirects_and_canonical(self):
  build.build(self.root)
  for old,new in build.LEGACY_REDIRECTS.items():
   page=self.text(old)
   self.assertIn('http-equiv="refresh" content="0;url='+build.SITE_URL+new+'"',page)
   self.assertIn('rel="canonical" href="'+build.SITE_URL+new+'"',page)
   self.assertNotIn('noindex',page)
  self.assertEqual(build.LEGACY_REDIRECTS['ja/about.html'],'profile.html')
  self.assertFalse((self.root/'dist/article/article_00.html').exists())
  self.assertNotIn('article/article_00.html',self.text('writing.html'))
  self.assertTrue((self.root/'dist/google1f49d64928618d22.html').is_file())
  sitemap=self.text('sitemap.xml')
  self.assertNotIn('/ja/',sitemap);self.assertNotIn('/en/',sitemap);self.assertNotIn('home.html',sitemap)
  for old in build.LEGACY_REDIRECTS:self.assertNotIn(build.SITE_URL+old+'<',sitemap)
  self.assertIn('rel="canonical" href="'+build.SITE_URL+'"',self.text('index.html'))
  for key in build.NAV:
   self.assertNotIn('noindex',self.text(key+'.html'))
   self.assertIn('alt="'+build.ILLUSTRATION_ALT[key]+'"',self.text(key+'.html'))
 def test_profile_lists_only_published_analyses(self):
  p=self.root/'content/site.json';site=build.read_json(p)
  site['analysis_topics']=[{'label':'Example topic','articles':['logistic-example','japanese-note','missing-article']}]
  p.write_text(json.dumps(site),encoding='utf-8')
  mp,m=self.meta('logistic-example');m['draft']=False;mp.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  profile=self.text('profile.html')
  self.assertIn('Selected analyses',profile);self.assertNotIn('Example topic',profile)
  # A Japanese original with an English translation is listed by its translation.
  self.assertIn('href="writing/logistic-example-en.html"',profile)
  self.assertNotIn('japanese-note',profile)
 def test_real_site_has_no_manually_assigned_topics(self):
  site=build.read_json(build.BASE/'content/site.json')
  self.assertNotIn('analysis_topics',site)
  self.assertTrue(all(path.startswith('topics/') for path in site['legacy_topic_paths']))
 def test_english_summary_and_social_metadata(self):
  p,m=self.meta('japanese-note');m.update(draft=False,updated='2026-09-30',english={'title':'English title','summary':'English summary.'});p.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  page=self.text('writing/japanese-note.html')
  self.assertIn('<section class="abstract" lang="en"',page);self.assertIn('English summary.',page)
  data=json.loads(re.search(r'application/ld\+json">(.*?)</script>',page)[1])
  self.assertEqual(data['dateModified'],'2026-09-30');self.assertEqual(data['datePublished'],'2026-09-26')
  self.assertEqual(data['alternativeHeadline'],'English title')
  self.assertIn('article:modified_time" content="2026-09-30"',page)
  p,m=self.meta('japanese-note');m['english']={'title':'x'};p.write_text(json.dumps(m),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'english'):build.load_articles(self.root/'content')
 def test_drafts_and_stale_files(self):
  build.build(self.root,preview=True);keep=self.root/'dist/manual.txt';keep.write_text('keep')
  self.assertTrue((self.root/'dist/writing/japanese-note.html').exists())
  build.build(self.root)
  self.assertFalse((self.root/'dist/writing/japanese-note.html').exists());self.assertTrue(keep.exists())
 def test_single_language_article(self):
  p,m=self.meta('japanese-note');m['draft']=False;p.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root,strict_translations=True)
  self.assertIn('lang="ja"',self.text('writing/japanese-note.html'))
  self.assertIn('writing/japanese-note.html',self.text('writing.html'))
  self.assertFalse((self.root/'dist/writing/japanese-note-en.html').exists())
 def test_optional_translation_review(self):
  p,m=self.meta('logistic-example');m['reviewed']={'en':build.fingerprint(p.parent,m)};p.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root,preview=True,strict_translations=True)
  with (p.parent/'shared/model.R').open('a') as f:f.write('\n# change\n')
  with self.assertRaises(ValueError):build.build(self.root,preview=True,strict_translations=True)
 def test_single_source_working_paper(self):
  p,m=self.meta('japanese-note');m['draft']=False;m['category']='paper';p.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  self.assertIn('writing/japanese-note.html',self.text('publication.html'))
 def test_local_links(self):
  build.build(self.root,preview=True)
  for path in (self.root/'dist').rglob('*.html'):
   parsed=Links();parsed.feed(path.read_text(encoding='utf-8'))
   for link in parsed.links:
    u=urlsplit(link)
    if u.scheme or u.netloc:continue
    target=(path.parent/unquote(u.path)).resolve() if u.path else path
    self.assertTrue(target.exists(),f'{path}: {link}')
    if u.fragment:
     p=Links();p.feed(target.read_text(encoding='utf-8'));self.assertIn(unquote(u.fragment),p.ids)
 def test_static_resources(self):
  build.build(self.root)
  for path in (self.root/'static').rglob('*'):
   if path.is_file():
    output=self.root/'dist'/path.relative_to(self.root/'static')
    self.assertTrue(output.is_file())
    if path.suffix in ('.pdf','.png','.ipynb'):self.assertEqual(path.read_bytes(),output.read_bytes())
  self.assertNotIn('site/',self.text('sitemap.xml'))
 def test_svg_assets_are_safe_and_well_formed(self):
  expected={'favicon.svg','model-isometric.svg','profile-isometric.svg','writing-isometric.svg','software-isometric.svg','publication-isometric.svg','activity-isometric.svg'}
  self.assertEqual(expected,{p.name for p in (self.root/'assets').glob('*.svg')})
  forbidden=('script','foreignobject')
  external=('http://','https://','//','data:','javascript:')
  for path in (self.root/'assets').glob('*.svg'):
   tree=ET.parse(path)
   for element in tree.iter():
    self.assertNotIn(element.tag.rsplit('}',1)[-1].lower(),forbidden,path.name)
    for key,value in element.attrib.items():
     name=key.rsplit('}',1)[-1].lower()
     self.assertFalse(name.startswith('on'),f'{path.name}: event handler {name}')
     if name=='href':self.assertFalse(value.lower().startswith(external),f'{path.name}: external reference')
 def test_sitemap_lastmod_feed_and_home_recent(self):
  p,m=self.meta('japanese-note');m.update(draft=False,date='2026-10-04',updated='2026-10-06');p.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','a':'http://www.w3.org/2005/Atom'}
  rows={u.find('s:loc',ns).text:u.find('s:lastmod',ns) for u in ET.fromstring(self.text('sitemap.xml')).findall('s:url',ns)}
  article=build.SITE_URL+'writing/japanese-note.html'
  self.assertEqual(rows[article].text,'2026-10-06')
  self.assertEqual(rows[build.SITE_URL+'writing.html'].text,'2026-10-06')
  self.assertIsNone(rows[build.SITE_URL+'profile.html'])
  feed=ET.fromstring(self.text('feed.xml'))
  ids=[e.find('a:id',ns).text for e in feed.findall('a:entry',ns)]
  self.assertIn(article,ids)
  self.assertEqual(len(ids),len(set(ids)))
  self.assertIn('Sitemap: '+build.SITE_URL+'feed.xml',self.text('robots.txt'))
  home=self.text('index.html')
  self.assertIn('application/atom+xml',home)
  self.assertIn('Recent writing',home);self.assertIn('writing/japanese-note.html',home)
  self.assertIn('PK/PD and Mathematical Biology',home);self.assertLessEqual(build.display_width(re.search(r'<title>(.*?)</title>',home)[1]),60)
  p,m=self.meta('japanese-note');m['updated']='2026-10-01';p.write_text(json.dumps(m),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'updated is before date'):build.build(self.root)
 def test_preview_has_no_feed(self):
  build.build(self.root,preview=True)
  self.assertFalse((self.root/'dist/feed.xml').exists())
  self.assertNotIn('application/atom+xml',self.text('index.html'))
 def test_shared_code_traversal(self):
  p=self.root/'content/articles/japanese-note/ja.md';p.write_text('{{code:r:../meta.json}}',encoding='utf-8')
  with self.assertRaises(ValueError):build.build(self.root,preview=True)
 def test_missing_article_body(self):
  p,m=self.meta('japanese-note');m['locales']['en']={'title':'English','summary':'Summary'};p.write_text(json.dumps(m),encoding='utf-8')
  with self.assertRaises(ValueError):build.build(self.root,preview=True)
 def test_figures_get_size_and_lazy_loading(self):
  import struct,zlib
  folder=self.root/'content/articles/logistic-example';(folder/'shared/figures').mkdir(parents=True,exist_ok=True)
  png=b'\x89PNG\r\n\x1a\n'+struct.pack('>I',13)+b'IHDR'+struct.pack('>IIBBBBB',640,480,8,2,0,0,0);png+=struct.pack('>I',zlib.crc32(png[12:29]))
  (folder/'shared/figures/a.png').write_bytes(png)
  (folder/'shared/figures/b.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200"></svg>',encoding='utf-8')
  self.assertEqual(build.image_size(folder/'shared/figures/a.png'),(640,480))
  self.assertEqual(build.image_size(folder/'shared/figures/b.svg'),(300,200))
  article=dict(folder=folder,slug='logistic-example')
  body=build.add_image_attributes('<img alt="a" src="shared/logistic-example/figures/a.png" /><img alt="b" src="shared/logistic-example/figures/b.svg" />',article)
  first,second=re.findall(r'<img[^>]*>',body)
  self.assertIn('width="640" height="480"',first);self.assertNotIn('lazy',first)
  self.assertIn('width="300" height="200"',second);self.assertIn('loading="lazy"',second)
 def test_article_lead_related_breadcrumb_and_llms(self):
  p=self.root/'content/site.json';site=build.read_json(p)
  site['analysis_topics']=[{'label':'Example','articles':['logistic-example','japanese-note']}]
  p.write_text(json.dumps(site),encoding='utf-8')
  for slug in ('logistic-example','japanese-note'):
   mp,m=self.meta(slug);m['draft']=False
   if slug=='japanese-note':m['english']={'title':'Logistic growth response','summary':'Logistic growth and population model response.'}
   mp.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  page=self.text('writing/japanese-note.html')
  _,m=self.meta('japanese-note')
  self.assertIn('<p class="lead">'+m['locales']['ja']['summary']+'</p>',page)
  self.assertIn('関連する解析',page);self.assertIn('href="logistic-example.html"',page)
  self.assertIn('"BreadcrumbList"',page)
  data=json.loads(re.search(r'application/ld\+json">(.*?)</script>',page)[1]);self.assertEqual(data['@type'],'Article')
  llms=self.text('llms.txt')
  self.assertIn('writing/japanese-note.html',llms);self.assertIn('(article in Japanese)',llms)
  build.build(self.root,preview=True)
  self.assertFalse((self.root/'dist/llms.txt').exists())

 def test_social_card_is_published_only_with_its_article(self):
  png=b'\x89PNG\r\n\x1a\n'+b'0'*20
  for slug in ('logistic-example','japanese-note'):
   (self.root/'content/articles'/slug/'og.png').write_bytes(png)
  mp,m=self.meta('logistic-example');m['draft']=False;mp.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  self.assertEqual((self.root/'dist/writing/og/logistic-example.png').read_bytes(),png)
  self.assertFalse((self.root/'dist/writing/og/japanese-note.png').exists())
  self.assertIn('writing/og/logistic-example.png',self.text('writing/logistic-example.html'))
  self.assertIn('assets/og-default.png',self.text('profile.html'))
 def test_seo_warnings_are_advisory(self):
  mp,m=self.meta('logistic-example');m['draft']=False
  m['locales']['en']['title']='A very long question title that search engines will certainly cut off somewhere';mp.write_text(json.dumps(m),encoding='utf-8')
  result=build.build(self.root)
  joined=' '.join(result['seo_warnings'])
  self.assertIn('Title is cut in search results',joined);self.assertIn('logistic-example/en',joined)
  self.assertIn('No social card (og.png)',joined)
  m['locales']['en']['seo_title']='Short question';mp.write_text(json.dumps(m),encoding='utf-8')
  self.assertNotIn('Title is cut in search results (',' '.join(w for w in build.build(self.root)['seo_warnings'] if 'logistic-example/en' in w))
  self.assertEqual(build.display_width('PK'),2);self.assertEqual(build.display_width('用量'),4)
 def test_search_text_does_not_unreview_a_translation(self):
  mp,m=self.meta('logistic-example')
  before=build.fingerprint(mp.parent,m)
  m['locales'][m['source_language']].update(seo_title='Shorter',seo_description='A shorter description that is long enough to be a description.')
  self.assertEqual(build.fingerprint(mp.parent,m),before)
  m['locales'][m['source_language']]['summary']+=' Changed.'
  self.assertNotEqual(build.fingerprint(mp.parent,m),before)
 def test_seo_text_must_be_non_empty(self):
  mp,m=self.meta('logistic-example');m['locales']['ja']['seo_title']=' ';mp.write_text(json.dumps(m),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'seo_title'):build.load_articles(self.root/'content',preview=True)

 def test_topic_pages_hubs_citation_and_llms(self):
  p=self.root/'content/site.json';site=build.read_json(p)
  site['analysis_topics']=[{'label':'Example topic','slug':'example-topic','description':'About the example topic.','articles':['logistic-example','japanese-note']},
                           {'label':'Hidden topic','slug':'hidden','description':'Nothing is live here.','articles':['missing-article']}]
  p.write_text(json.dumps(site),encoding='utf-8')
  for slug in ('logistic-example','japanese-note'):
   mp,m=self.meta(slug);m['draft']=False;mp.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  network=json.loads(self.text('assets/article-network.json'))
  group=next(g for g in network['clusters'] if 'logistic-example' in g['articles'])
  hub=self.text(group['href'])
  self.assertIn('Automatically detected',hub);self.assertIn('writing/logistic-example-en.html',hub)
  self.assertIn('CollectionPage',hub);self.assertIn('BreadcrumbList',hub)
  self.assertFalse((self.root/'dist/topics/hidden.html').exists())
  self.assertIn(group['href'],self.text('sitemap.xml'));self.assertNotIn('topics/hidden.html',self.text('sitemap.xml'))
  self.assertIn('href="'+group['href']+'"',self.text('profile.html'));self.assertIn('By topic',self.text('writing.html'))
  article=self.text('writing/japanese-note.html')
  self.assertIn('href="../topics/cluster-',article);self.assertIn('Kumakura, D. (2026). ',article);self.assertIn('Cite this article',article) if 'lang="en"' in article.split('<article')[1][:60] else self.assertIn('引用',article)
  llms=self.text('llms.txt')
  for expected in ('## Topics','## Identity','Kumakura Daiki','Cluster 1'):self.assertIn(expected,llms)
  self.assertNotIn('Example topic',llms)
 def test_legacy_topic_path_is_validated(self):
  p=self.root/'content/site.json';site=build.read_json(p)
  site['legacy_topic_paths']=['../Bad Slug']
  p.write_text(json.dumps(site),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'legacy topic path'):build.build(self.root,preview=True)

 def test_language_sitemap_and_live_topic_map(self):
  p=self.root/'content/site.json';site=build.read_json(p)
  site['analysis_topics']=[{'label':'Example','slug':'example','description':'Example topic.','articles':['logistic-example','japanese-note']}]
  p.write_text(json.dumps(site),encoding='utf-8')
  mp,m=self.meta('logistic-example');m['draft']=False;mp.write_text(json.dumps(m),encoding='utf-8')
  build.build(self.root)
  ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'}
  rows=ET.fromstring(self.text('sitemap.xml')).findall('s:url',ns)
  for row in rows:
   if '/writing/logistic-example' in row.find('s:loc',ns).text:
    alternatives={a.attrib['hreflang']:a.attrib['href'] for a in row.findall('x:link',ns)}
    self.assertEqual(set(alternatives),{'ja','en','x-default'})
    self.assertEqual(alternatives['en'],alternatives['x-default'])
  page=self.text('writing.html')
  data=json.loads(re.search(r'id="topic-map-data">(.*?)</script>',page)[1])
  self.assertEqual(data['article_count'],1)
  self.assertEqual(len(data['nodes']),1)
  self.assertNotIn('japanese-note',json.dumps(data))
  original=self.text('writing/logistic-example.html');translated=self.text('writing/logistic-example-en.html')
  schema=lambda html:json.loads(re.search(r'application/ld\+json">(.*?)</script>',html)[1])
  self.assertIn('workTranslation',schema(original));self.assertNotIn('translationOfWork',schema(original))
  self.assertIn('translationOfWork',schema(translated));self.assertNotIn('workTranslation',schema(translated))

 def test_scheduled_articles_do_not_influence_network_until_publication(self):
  mp,m=self.meta('logistic-example');m['draft']=False;mp.write_text(json.dumps(m),encoding='utf-8')
  mp,m=self.meta('japanese-note');m.update(draft=False,date='2099-01-01',publish_at='2099-01-01T09:00:00+09:00')
  mp.write_text(json.dumps(m),encoding='utf-8');build.build(self.root)
  before=self.text('assets/article-network.json')
  m['english']={'title':'Unpublished sentinel','summary':'Unpublished sentinel kinase occupancy.'}
  mp.write_text(json.dumps(m),encoding='utf-8');build.build(self.root)
  self.assertEqual(before,self.text('assets/article-network.json'))
  m.update(date='2000-01-01',publish_at='2000-01-01T09:00:00+09:00')
  mp.write_text(json.dumps(m),encoding='utf-8');build.build(self.root)
  after=json.loads(self.text('assets/article-network.json'))
  self.assertEqual(after['article_count'],2)
  self.assertIn('japanese-note',{node['id'] for node in after['nodes']})
  self.assertIn('data-article-cluster=',self.text('writing.html'))
  legacy=build.read_json(self.root/'content/site.json')['legacy_topic_paths'][0]
  self.assertIn('writing.html#by-topic',self.text(legacy))
  self.assertNotIn(build.SITE_URL+legacy+'<',self.text('sitemap.xml'))

 def test_software_pages(self):
  build.build(self.root)
  site=build.read_json(self.root/'content/site.json')
  for sw in site['software']:
   url='software/'+sw['slug']+'.html'
   page=self.text(url)
   for expected in (sw['id'],sw['url'],'SoftwareSourceCode','BreadcrumbList',sw['summary']):self.assertIn(expected,page,url)
   self.assertIn(url,self.text('software.html'));self.assertIn(url,self.text('sitemap.xml'))
   self.assertIn(sw['id'],self.text('llms.txt'))
  self.assertIn('remotes::install_github',self.text('software/pkident.html'))
 def test_software_page_needs_a_summary_of_search_length(self):
  p=self.root/'content/site.json';site=build.read_json(p)
  site['software'][0]['summary']='Too short.';p.write_text(json.dumps(site),encoding='utf-8')
  with self.assertRaisesRegex(ValueError,'software page'):build.build(self.root,preview=True)

 def test_robots_lists_extra_documentation_sitemaps_but_not_in_preview(self):
  build.build(self.root)
  robots=self.text('robots.txt')
  self.assertIn('Sitemap: '+build.SITE_URL+'sitemap.xml',robots)
  for path in build.EXTRA_SITEMAPS:self.assertIn('Sitemap: '+build.SITE_URL+path,robots)
  build.build(self.root,preview=True)
  preview=self.text('robots.txt');self.assertIn('Disallow: /',preview);self.assertNotIn('Sitemap',preview)

 def add_term(self,slug='sample-term',kind='term',related=('japanese-note',),**changes):
  folder=self.root/'content/reference'/slug;folder.mkdir(parents=True)
  locale=lambda lang:dict(title='Sample term' if lang=='en' else '用語の例',summary='A short definition that is long enough to serve as the page summary.' if lang=='en' else '要約の例',seo_title='Sample term' if lang=='en' else '用語の例',seo_description='A description of the sample term.' if lang=='en' else '用語の説明',faq=[dict(q='What is it?' if lang=='en' else '何ですか。',a='An example.' if lang=='en' else '例です。')])
  meta=dict(kind=kind,updated='2026-10-22',related_articles=list(related),locales=dict(en=locale('en'),ja=locale('ja')));meta.update(changes)
  (folder/'meta.json').write_text(json.dumps(meta,ensure_ascii=False),encoding='utf-8')
  (folder/'en.md').write_text('## Definition'+chr(10)*2+'Text.'+chr(10),encoding='utf-8');(folder/'ja.md').write_text('## 定義'+chr(10)*2+'本文。'+chr(10),encoding='utf-8')
 def test_reference_pages_publish_in_both_languages_with_structured_data(self):
  p,m=self.meta('japanese-note');m.update(draft=False,date='2026-10-04',publish_at='2026-10-04T09:00:00+09:00');p.write_text(json.dumps(m),encoding='utf-8')
  self.add_term();build.build(self.root)
  en=self.text('glossary/sample-term.html');ja=self.text('glossary/sample-term-ja.html')
  self.assertIn('<html lang="en">',en);self.assertIn('<html lang="ja">',ja)
  self.assertIn('hreflang="ja" href="'+build.SITE_URL+'glossary/sample-term-ja.html"',en);self.assertIn('hreflang="x-default"',en)
  self.assertIn('"@type": "DefinedTerm"',en.replace('"@type":"DefinedTerm"','"@type": "DefinedTerm"'));self.assertIn('FAQPage',en);self.assertIn('What is it?',en)
  self.assertIn('FAQPage',ja)
  self.assertIn('Sample term',self.text('reference.html'))
  self.assertIn(build.SITE_URL+'glossary/sample-term-ja.html',self.text('sitemap.xml'));self.assertIn(build.SITE_URL+'glossary/sample-term.html',self.text('llms.txt'))
  self.assertIn('href="../writing/',en)
 def test_tool_page_is_a_web_application(self):
  self.add_term('sample-tool','tool');build.build(self.root)
  self.assertIn('WebApplication',self.text('tools/sample-tool.html'))
 def test_reference_page_needs_both_languages_and_known_articles(self):
  self.add_term('one-language',locales=dict(en=dict(title='x',summary='x',seo_title='x',seo_description='x')))
  with self.assertRaisesRegex(ValueError,'both ja and en'):build.build(self.root)
  shutil.rmtree(self.root/'content/reference/one-language');self.add_term('unknown-link',related=('no-such-article',))
  with self.assertRaisesRegex(ValueError,'Unknown related article'):build.build(self.root)
 def test_reference_is_absent_when_there_are_no_pages(self):
  build.build(self.root);self.assertFalse((self.root/'dist/glossary').exists())

if __name__=='__main__':unittest.main()


