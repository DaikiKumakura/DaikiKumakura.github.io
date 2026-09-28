import unittest

from notify_indexnow import SITE_URL, urls_from_sitemap


class IndexNowTests(unittest.TestCase):
    def test_reads_only_canonical_site_urls(self):
        xml = b'''<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://daikikumakura.github.io/</loc></url><url><loc>https://daikikumakura.github.io/profile.html</loc></url></urlset>'''
        self.assertEqual(urls_from_sitemap(xml), [SITE_URL, SITE_URL + 'profile.html'])

    def test_rejects_another_host(self):
        xml = b'''<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://example.com/</loc></url></urlset>'''
        with self.assertRaises(ValueError):
            urls_from_sitemap(xml)


if __name__ == '__main__':
    unittest.main()

