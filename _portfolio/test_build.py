import json
import shutil
import tempfile
import unittest
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import build

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.lang=None
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag=='html': self.lang=attrs.get('lang')
        for key in ('href','src'):
            if key in attrs: self.links.append(attrs[key])

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        for name in ('content','templates','assets'):
            shutil.copytree(build.BASE/name,self.root/name)
    def tearDown(self): self.temp.cleanup()
    def text(self,name): return (self.root/'dist'/name).read_text(encoding='utf-8')
    def article_meta(self,slug='logistic-example'):
        p=self.root/'content/articles'/slug/'meta.json'
        return p,build.read_json(p)
    def test_migration_coverage_and_rendering(self):
        site=build.read_json(self.root/'content/site.json')
        ids={a['id'] for a in site['activities']}
        self.assertEqual(ids,{f'C{i}' for i in range(1,56)}|{f'G{i}' for i in range(2,11)}|{'N1','N2','N3','N4','E1','E2'})
        self.assertEqual(len(site['publications']),10)
        self.assertEqual(sum(p['kind']=='journal' for p in site['publications']),6)
        self.assertEqual(len(site['awards']),1)
        build.build(self.root,preview=True)
        for lang in build.LANGS:
            pub=self.text(f'{lang}/publications.html')
            self.assertIn('<strong>Daiki Kumakura</strong>',pub)
            self.assertLess(pub.index('id="preprint"'),pub.index('id="rlr-2021"'))
            activities=self.text(f'{lang}/activities.html')
            for id in ids:self.assertIn(f'id="activity-{id}"',activities)
            self.assertNotIn(build.UI[lang]['partial'],activities)
        host=next(a for a in site['activities'] if a['id']=='C54')
        self.assertEqual(host['role']['en'],'Host')
        self.assertFalse(host['authors']['en'])
    def test_drafts_excluded_and_stale_outputs_removed(self):
        build.build(self.root,preview=True)
        unrelated=self.root/'dist/manual.txt';unrelated.write_text('keep')
        build.build(self.root)
        self.assertFalse((self.root/'dist/ja/writing/logistic-example.html').exists())
        self.assertNotIn('logistic-example',self.text('ja/writing.html'))
        self.assertTrue(unrelated.exists())
    def test_missing_translation_not_fabricated(self):
        build.build(self.root,preview=True)
        self.assertFalse((self.root/'dist/en/writing/japanese-note.html').exists())
        self.assertIn('../ja/writing/japanese-note.html',self.text('en/writing.html'))
        self.assertIn('未翻訳',self.text('ja/writing/japanese-note.html'))
    def test_translation_review_and_invalidation(self):
        p,m=self.article_meta();m['reviewed']={'en':build.fingerprint(p.parent,m)}
        p.write_text(json.dumps(m),encoding='utf-8')
        self.assertEqual(build.build(self.root,preview=True,strict_translations=True)['warnings'],[])
        with (p.parent/'shared/model.R').open('a') as f:f.write('\n# changed\n')
        with self.assertRaises(ValueError):build.build(self.root,preview=True,strict_translations=True)
        build.build(self.root,preview=True)
        self.assertIn('translation needs review',self.text('en/writing/logistic-example.html'))
    def test_shared_code_and_metadata_propagate(self):
        code=self.root/'content/articles/logistic-example/shared/model.R'
        code.write_text('unique_marker <- 42\n',encoding='utf-8')
        sitepath=self.root/'content/site.json';site=build.read_json(sitepath)
        site['publications'][0]['venue']='UNIQUE SHARED VENUE'
        sitepath.write_text(json.dumps(site),encoding='utf-8')
        build.build(self.root,preview=True)
        for lang in build.LANGS:
            self.assertIn('unique_marker &lt;- 42',self.text(f'{lang}/writing/logistic-example.html'))
            for page in ('index','publications'):
                self.assertIn('UNIQUE SHARED VENUE',self.text(f'{lang}/{page}.html'))
    def test_local_links_and_language_metadata(self):
        build.build(self.root,preview=True)
        for path in (self.root/'dist').rglob('*.html'):
            parser=Links();parser.feed(path.read_text(encoding='utf-8'))
            self.assertIn(parser.lang,build.LANGS)
            for link in parser.links:
                part=urlsplit(link)
                if part.scheme or part.netloc:continue
                target=(path.parent/unquote(part.path)).resolve() if part.path else path
                self.assertTrue(target.exists(),f'{path}: {link}')
                if part.fragment:
                    q=Links();q.feed(target.read_text(encoding='utf-8'))
                    self.assertIn(unquote(part.fragment),q.ids)
    def test_working_paper_uses_single_record(self):
        p,m=self.article_meta('japanese-note');m['category']='paper';m['draft']=False
        p.write_text(json.dumps(m),encoding='utf-8')
        build.build(self.root)
        for lang in build.LANGS:
            self.assertIn('../ja/writing/japanese-note.html',self.text(f'{lang}/publications.html'))
    def test_publication_metadata_and_legacy_routes(self):
        build.build(self.root,strict_translations=True)
        self.assertNotIn('logistic-example',(self.root/'dist/sitemap.xml').read_text())
        for old,target in build.LEGACY_REDIRECTS.items():
            self.assertIn(build.SITE_URL+target,self.text(old))
        for lang in build.LANGS:
            page=self.text(f'{lang}/index.html')
            self.assertIn(f'rel="canonical" href="{build.SITE_URL}{lang}/index.html"',page)
            self.assertNotIn('noindex',page)
            self.assertNotIn('Prototype preview',page)
        self.assertNotIn('Disallow: /',(self.root/'dist/robots.txt').read_text())
    def test_missing_fixed_translation_fails(self):
        p=self.root/'content/site.json';s=build.read_json(p);del s['profile']['en']
        p.write_text(json.dumps(s),encoding='utf-8')
        with self.assertRaises(ValueError):build.build(self.root)
    def test_shared_code_traversal_rejected(self):
        p=self.root/'content/articles/japanese-note/ja.md'
        p.write_text('{{code:r:../meta.json}}',encoding='utf-8')
        with self.assertRaises(ValueError):build.build(self.root,preview=True)
    def test_missing_translation_body_fails(self):
        p,m=self.article_meta('japanese-note');m['locales']['en']={'title':'English','summary':'Summary'}
        p.write_text(json.dumps(m),encoding='utf-8')
        with self.assertRaises(ValueError):build.build(self.root,preview=True)

if __name__=='__main__':unittest.main()
