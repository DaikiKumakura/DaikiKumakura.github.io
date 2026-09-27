import json
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
  for n in ('content','templates','assets','static'):shutil.copytree(build.BASE/n,self.root/n)
  shutil.copytree(build.BASE/'fixtures/articles',self.root/'content/articles')
 def tearDown(self):self.temp.cleanup()
 def text(self,name):return (self.root/'dist'/name).read_text(encoding='utf-8')
 def meta(self,slug):
  p=self.root/'content/articles'/slug/'meta.json';return p,build.read_json(p)
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
  profile=self.text('profile.html')
  self.assertNotIn('Best Award',profile);self.assertNotIn('Functional Specialization',profile)
  positions=[home.index('>'+label+'</a>') for label in build.NAV.values()]
  self.assertEqual(positions,sorted(positions))
 def test_legacy_redirects_and_canonical(self):
  build.build(self.root)
  for old,new in build.LEGACY_REDIRECTS.items():self.assertIn(build.SITE_URL+new,self.text(old))
  sitemap=self.text('sitemap.xml')
  self.assertNotIn('/ja/',sitemap);self.assertNotIn('/en/',sitemap);self.assertNotIn('home.html',sitemap)
  self.assertIn('rel="canonical" href="'+build.SITE_URL+'"',self.text('index.html'))
  for key in build.NAV:
   self.assertNotIn('noindex',self.text(key+'.html'))
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
 def test_shared_code_traversal(self):
  p=self.root/'content/articles/japanese-note/ja.md';p.write_text('{{code:r:../meta.json}}',encoding='utf-8')
  with self.assertRaises(ValueError):build.build(self.root,preview=True)
 def test_missing_article_body(self):
  p,m=self.meta('japanese-note');m['locales']['en']={'title':'English','summary':'Summary'};p.write_text(json.dumps(m),encoding='utf-8')
  with self.assertRaises(ValueError):build.build(self.root,preview=True)

if __name__=='__main__':unittest.main()
