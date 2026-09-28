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
        self.assertEqual(data['mainEntity']['sameAs'], [site['github'], site['orcid'], site['linkedin']])
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

if __name__ == '__main__':
    unittest.main()



