import unittest
from citations import link_numbered_references

class CitationTests(unittest.TestCase):
    def test_links_only_existing_numbered_references(self):
        s='<p>Results [1, 2] and ［2］; unknown [9]. <code>arr[1]</code> <a href="https://example.org">[1]</a></p><h2>参考文献</h2><ol><li><a href="https://one.example">One</a></li><li><a href="https://two.example">Two</a></li></ol>'
        out=link_numbered_references(s)
        self.assertIn('(<a class="reference-link" href="#ref-1">1</a>, <a class="reference-link" href="#ref-2">2</a>)',out)
        self.assertIn('unknown [9]',out);self.assertIn('<code>arr[1]</code>',out)
        self.assertIn('<a href="https://example.org">[1]</a>',out)
        self.assertIn('<li id="ref-1">',out);self.assertIn('<li id="ref-2">',out)
    def test_ambiguous_reference_sections_are_left_untouched(self):
        s='<p>Text [1].</p><h2>References</h2><ol><li>Outer<ol><li>Nested</li></ol></li></ol>'
        self.assertEqual(link_numbered_references(s),s)
    def test_adjacent_citations_locators_and_intervals(self):
        s='<p>paper[1]; [2, Table 11]; [1–2]; interval [4339–14142].</p><h2>文献</h2><ol><li>One</li><li>Two</li></ol>'
        out=link_numbered_references(s)
        self.assertIn('paper(<a class="reference-link" href="#ref-1">1</a>)',out)
        self.assertIn('(<a class="reference-link" href="#ref-2">2</a>, Table 11)',out)
        self.assertIn('(<a class="reference-link" href="#ref-1">1</a>–<a class="reference-link" href="#ref-2">2</a>)',out)
        self.assertIn('interval [4339–14142]',out)
