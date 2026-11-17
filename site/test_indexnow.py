import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from notify_indexnow import SITEMAP_URL, SITE_URL, changed_urls, notify, urls_from_sitemap


class IndexNowTests(unittest.TestCase):
    def test_reads_only_canonical_site_urls(self):
        xml = b'''<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://daikikumakura.github.io/</loc></url><url><loc>https://daikikumakura.github.io/profile.html</loc></url></urlset>'''
        self.assertEqual(urls_from_sitemap(xml), [SITE_URL, SITE_URL + 'profile.html'])

    def test_rejects_another_host(self):
        xml = b'''<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://example.com/</loc></url></urlset>'''
        with self.assertRaises(ValueError):
            urls_from_sitemap(xml)

    def test_diff_notifies_additions_edits_and_removals(self):
        a, b, c, d = [SITE_URL + name for name in ('a', 'b', 'c', 'd')]
        old = {SITEMAP_URL: {a: {'sha256': 'same', 'etag': 'old'},
                             b: {'sha256': 'before'}, c: {'sha256': 'removed'}}}
        new = {SITEMAP_URL: {a: {'sha256': 'same', 'etag': 'new'},
                             b: {'sha256': 'after'}, d: {'sha256': 'added'}}}
        self.assertEqual(changed_urls(old, new), [b, c, d])
        self.assertEqual(changed_urls({}, new), [a, b, d])
        self.assertEqual(changed_urls(new, new), [])

    def test_failed_submission_leaves_retry_baseline_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / 'accepted.json'
            previous = {SITEMAP_URL: {SITE_URL: {'sha256': 'old'}}}
            current = {SITEMAP_URL: {SITE_URL: {'sha256': 'new'}}}
            state.write_text(json.dumps(previous), encoding='utf-8')
            with patch('notify_indexnow.snapshots', return_value=current), patch(
                'notify_indexnow.submit', side_effect=[RuntimeError('rejected'), None]
            ) as submit:
                with self.assertRaises(RuntimeError):
                    notify(Path(directory), state)
                self.assertEqual(json.loads(state.read_text(encoding='utf-8')), previous)
                self.assertTrue(notify(Path(directory), state))
                self.assertFalse(notify(Path(directory), state))
                self.assertEqual(submit.call_count, 2)
                self.assertEqual(json.loads(state.read_text(encoding='utf-8')), current)


if __name__ == '__main__':
    unittest.main()

