import unittest

from check_dropped_urls import dropped


class DroppedUrlTests(unittest.TestCase):
    def test_only_missing_article_urls_are_reported(self):
        live = {'https://x.test/', 'https://x.test/profile.html', 'https://x.test/writing/a.html', 'https://x.test/writing/b.html'}
        built = {'https://x.test/', 'https://x.test/writing/a.html'}
        self.assertEqual(dropped(live, built), ['https://x.test/writing/b.html'])

    def test_new_articles_and_unchanged_sites_report_nothing(self):
        live = {'https://x.test/writing/a.html'}
        self.assertEqual(dropped(live, live | {'https://x.test/writing/new.html'}), [])
        self.assertEqual(dropped(set(), {'https://x.test/writing/a.html'}), [])


if __name__ == '__main__':
    unittest.main()
