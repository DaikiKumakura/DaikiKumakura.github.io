import json
import re
import unittest
from pathlib import Path
from seo import DESCRIPTIONS, enrich

class MetadataTests(unittest.TestCase):
    def test_page_descriptions_have_search_friendly_lengths(self):
        for key, description in DESCRIPTIONS.items():
            self.assertGreaterEqual(len(description), 80, key)
            self.assertLessEqual(len(description), 160, key)

    def test_profile_identity_and_safe_json(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        page = '<head><title>About | Daiki Kumakura</title><meta name="description" content="old"></head>'
        result = enrich(page, 'profile.html', site, 'https://daikikumakura.github.io/')
        data = json.loads(re.search(r'application/ld\+json">(.*?)</script>', result)[1])
        self.assertEqual(data['@type'], 'ProfilePage')
        self.assertEqual(data['mainEntity']['sameAs'], [site['github'], site['qiita'], site['docker'], site['orcid'], site['scholar'], site['linkedin']])
        self.assertNotIn('worksFor', data['mainEntity'])
        self.assertEqual(result.count('name="description"'), 1)

    def test_article_title_is_not_double_escaped(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        result = enrich('<head><title>A &amp; B</title><meta name="description" content="A &amp; B"></head>', 'writing/example.html', site, 'https://daikikumakura.github.io/')
        self.assertIn('<title>A &amp; B</title>', result)
        self.assertNotIn('&amp;amp;', result)

    def test_software_schema_describes_visible_projects(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        page = '<head><title>Software | Daiki Kumakura</title><meta name="description" content="old"></head>'
        result = enrich(page, 'software.html', site, 'https://daikikumakura.github.io/')
        data = json.loads(re.search(r'application/ld\+json">(.*?)</script>', result)[1])
        self.assertEqual(data['@type'], 'CollectionPage')
        items = data['mainEntity']['itemListElement']
        self.assertEqual([x['item']['name'] for x in items], [x['id'] for x in site['software']])
        self.assertTrue(all(x['item']['@type'] == 'SoftwareSourceCode' for x in items))
        self.assertNotIn('worksFor', data['about'])

    def test_article_social_image_uses_first_raster_figure(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        page = '<head><title>T</title><meta name="description" content="d"></head><body><img src="shared/x/a.svg" alt="a"><img src="shared/x/b.png" alt="b"></body>'
        result = enrich(page, 'writing/x.html', site, 'https://daikikumakura.github.io/', {'date': '2026-10-01'})
        self.assertIn('<meta property="og:image" content="https://daikikumakura.github.io/writing/shared/x/b.png">', result)
        self.assertIn('summary_large_image', result)
        data = json.loads(re.search(r'application/ld\+json">(.*?)</script>', result)[1])
        self.assertEqual(data['dateModified'], '2026-10-01')
        # SVG figures cannot be used for social previews, so the site-wide card is used.
        plain = enrich('<head><title>T</title><meta name="description" content="d"></head><body><img src="a.svg" alt="a"></body>', 'writing/y.html', site, 'https://daikikumakura.github.io/')
        self.assertIn('<meta property="og:image" content="https://daikikumakura.github.io/assets/og-default.png">', plain)
        self.assertIn('summary_large_image', plain)

    def test_social_card_beats_the_first_figure(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        page = '<head><title>Long title | Daiki Kumakura</title><meta name="description" content="d"></head><body><img src="shared/x/b.png" alt="b" width="1800" height="1260"></body>'
        result = enrich(page, 'writing/x.html', site, 'https://daikikumakura.github.io/', {'date': '2026-10-01'}, 'writing/og/x.png')
        self.assertIn('og:image" content="https://daikikumakura.github.io/writing/og/x.png"', result)
        self.assertIn('og:image:width" content="1200"', result)
        self.assertIn('og:image:height" content="630"', result)
        data = json.loads(re.search(r'application/ld\+json">(.*?)</script>', result)[1])
        self.assertEqual(data['image'][0], 'https://daikikumakura.github.io/writing/og/x.png')

    def test_site_pages_use_the_default_card(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        for name in ('index.html', 'profile.html', 'writing.html'):
            page = '<html lang="en"><head><title>Profile | Daiki Kumakura</title><meta name="description" content="x"></head></html>'
            result = enrich(page, name, site, 'https://daikikumakura.github.io/')
            self.assertIn('og:image" content="https://daikikumakura.github.io/assets/og-default.png"', result, name)
            self.assertIn('og:image:alt', result)
        self.assertTrue((Path(__file__).parent/'assets/og-default.png').is_file())

    def test_seo_text_shortens_title_and_description_only(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        page = '<html lang="en"><head><title>A very long research question about dosing | Daiki Kumakura</title><meta name="description" content="Long summary."></head></html>'
        meta = {'date': '2026-10-01', 'locales': {'en': {'title': 'x', 'summary': 'y', 'seo_title': 'Short title', 'seo_description': 'Short description.'}}}
        result = enrich(page, 'writing/x.html', site, 'https://daikikumakura.github.io/', meta)
        self.assertIn('<title>Short title</title>', result)
        self.assertIn('og:title" content="Short title"', result)
        self.assertIn('<meta name="description" content="Short description.">', result)
        article, crumbs = (json.loads(blob) for blob in re.findall(r'application/ld\+json">(.*?)</script>', result))
        self.assertEqual(article['headline'], 'A very long research question about dosing')
        self.assertEqual(crumbs['itemListElement'][2]['name'], 'A very long research question about dosing')
        untouched = enrich(page, 'writing/x.html', site, 'https://daikikumakura.github.io/', {'date': '2026-10-01', 'locales': {'en': {'title': 'x', 'summary': 'y'}}})
        self.assertIn('<title>A very long research question about dosing | Daiki Kumakura</title>', untouched)

    def test_person_has_every_name_and_a_third_person_description(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        result = enrich('<head><title>Profile | Daiki Kumakura</title><meta name="description" content="x"></head>', 'profile.html', site, 'https://daikikumakura.github.io/')
        person = json.loads(result.split('application/ld+json">')[1].split('</script>')[0])['mainEntity']
        self.assertIn('Kumakura Daiki', person['alternateName'])
        self.assertIn('熊倉大騎', person['alternateName'])
        self.assertTrue(person['description'].startswith('Daiki Kumakura'))
        self.assertEqual(person['identifier']['value'], '0000-0001-9859-0720')
        self.assertEqual(person['knowsLanguage'], ['ja', 'en'])

    def test_translated_pair_gets_x_default_and_author(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        page = '<html lang="en"><head><title>T</title><meta name="description" content="d"><link rel="alternate" hreflang="ja" href="x.html"><link rel="alternate" hreflang="en" href="x-en.html"></head></html>'
        result = enrich(page, 'writing/x-en.html', site, 'https://daikikumakura.github.io/', {'date': '2026-10-01'})
        self.assertIn('hreflang="x-default" href="https://daikikumakura.github.io/writing/x-en.html"', result)
        self.assertIn('<meta name="author" content="Daiki Kumakura">', result)
        single = enrich('<html lang="en"><head><title>T</title><meta name="description" content="d"><link rel="alternate" hreflang="en" href="y.html"></head></html>', 'writing/y.html', site, 'https://daikikumakura.github.io/', {'date': '2026-10-01'})
        self.assertNotIn('x-default', single)

    def test_article_schema_names_topics_and_free_access(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        result = enrich('<head><title>T | Daiki Kumakura</title><meta name="description" content="d"></head>', 'writing/x.html', site, 'https://daikikumakura.github.io/', {'date': '2026-10-01'}, None, ['Topic A'])
        article = json.loads(result.split('application/ld+json">')[1].split('</script>')[0])
        self.assertTrue(article['isAccessibleForFree'])
        self.assertEqual(article['keywords'], ['Topic A'])
        self.assertEqual(article['publisher'], {'@id': 'https://daikikumakura.github.io/#person'})

    def test_publications_are_scholarly_articles_with_doi(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        result = enrich('<head><title>Publication | Daiki Kumakura</title><meta name="description" content="x"></head>', 'publication.html', site, 'https://daikikumakura.github.io/')
        items = json.loads(result.split('application/ld+json">')[1].split('</script>')[0])['mainEntity']['itemListElement']
        self.assertEqual(len(items), len(site['publications']))
        for entry in items:
            self.assertIn(entry['item']['@type'], ('ScholarlyArticle', 'Thesis'))
            self.assertEqual(entry['item']['identifier']['propertyID'], 'DOI')
            self.assertTrue(entry['item']['datePublished'].isdigit())

    def test_topic_page_schema(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        result = enrich('<html lang="en"><head><title>Example topic | Daiki Kumakura</title><meta name="description" content="About it."></head></html>', 'topics/example.html', site, 'https://daikikumakura.github.io/')
        blobs = [json.loads(b.split('</script>')[0]) for b in result.split('application/ld+json">')[1:]]
        self.assertEqual([b['@type'] for b in blobs], ['CollectionPage', 'BreadcrumbList'])
        self.assertEqual(blobs[0]['name'], 'Example topic')
        self.assertEqual(blobs[1]['itemListElement'][2]['item'], 'https://daikikumakura.github.io/topics/example.html')

    def test_software_page_schema(self):
        site = json.loads((Path(__file__).parent/'content/site.json').read_text(encoding='utf-8'))
        result = enrich('<html lang="en"><head><title>pkident | Daiki Kumakura</title><meta name="description" content="x"></head></html>', 'software/pkident.html', site, 'https://daikikumakura.github.io/')
        blobs = [json.loads(b.split('</script>')[0]) for b in result.split('application/ld+json">')[1:]]
        self.assertEqual([b['@type'] for b in blobs], ['SoftwareSourceCode', 'BreadcrumbList'])
        self.assertEqual(blobs[0]['codeRepository'], 'https://github.com/DaikiKumakura/pkident')
        self.assertEqual(blobs[0]['programmingLanguage'], 'R')
        self.assertEqual(blobs[1]['itemListElement'][1]['item'], 'https://daikikumakura.github.io/software.html')

if __name__ == '__main__':
    unittest.main()



