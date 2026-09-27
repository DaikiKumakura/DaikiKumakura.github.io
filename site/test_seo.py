import json
import re
import unittest
from pathlib import Path
from seo import enrich

class MetadataTests(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()

