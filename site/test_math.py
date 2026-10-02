"""Regression coverage for TeX escaping through Markdown and the shared template."""
from pathlib import Path
import tempfile
import unittest
import build
import json
import re
from seo import enrich


class MathRenderingTests(unittest.TestCase):
    def test_preserves_math_but_leaves_code_literal(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / 'ja.md').write_text(
                r'Inline \(A_1+A_2\).' + '\n\n' +
                r'\[\Omega=\begin{pmatrix}1&0\\0&1\end{pmatrix}\]' + '\n\n' +
                '```text\n' + r'\(code_only\)' + '\n```\n', encoding='utf-8')
            rendered, _ = build.render_body({'folder': folder, 'meta': {'math': True}}, 'ja')
            self.assertIn(r'\(A_1+A_2\)', rendered)
            self.assertIn(r'1&amp;0\\0&amp;1', rendered)
            self.assertEqual(rendered.count('class="math"'), 2)
            self.assertIn(r'<code class="language-text">\(code_only\)', rendered)

    def test_template_uses_single_runtime_backslash(self):
        template = (build.BASE / 'templates/base.html').read_text(encoding='utf-8')
        self.assertIn(r"inlineMath:[['\\(','\\)']]", template)
        self.assertNotIn(r"inlineMath:[['\\\\(','\\\\)']]", template)

    def test_article_schema_matches_visible_language_and_citations(self):
        site = json.loads((build.BASE / 'content/site.json').read_text(encoding='utf-8'))
        page = '<html lang="ja"><head><title>PK | Daiki Kumakura</title><meta name="description" content="PK study"></head><p class="meta">Daiki Kumakura · 2026-10-02 · Tutorial</p><a href="https://doi.org/10.1111/cts.13825">Paper</a><img src="shared/study/pk.svg"></html>'
        rendered = enrich(page, 'writing/study.html', site, build.SITE_URL)
        data = json.loads(re.search(r'application/ld\+json">(.*?)</script>', rendered)[1])
        self.assertEqual(data['@type'], 'Article')
        self.assertEqual(data['inLanguage'], 'ja')
        self.assertEqual(data['datePublished'], '2026-10-02')
        self.assertEqual(data['citation'], ['https://doi.org/10.1111/cts.13825'])
        self.assertEqual(data['image'], [build.SITE_URL + 'writing/shared/study/pk.svg'])
