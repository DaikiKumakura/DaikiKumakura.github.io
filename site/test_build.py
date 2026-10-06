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
   shutil.copytree(build.BASE/n,self.root/n,ignore=shutil.ignore_patterns('articles') if n=='content' else None)
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
  self.assertIn('Selected analyses',profile);self.assertIn('Example topic',profile)
  self.assertIn('href="writing/logistic-example.html"',profile)
  self.assertNotIn('japanese-note',profile)
 def test_real_analysis_topics_name_existing_articles(self):
  site=build.read_json(build.BASE/'content/site.json')
  for topic in site['analysis_topics']:
   for slug in topic['articles']:self.assertTrue((build.BASE/'content/articles'/slug/'meta.json').is_file(),slug)
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
  self.assertIn('Mathematical Biology and PK/PD Modeling',home)
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

if __name__=='__main__':unittest.main()


