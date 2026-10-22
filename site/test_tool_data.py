import unittest
import make_tool_data


class ToolDataTests(unittest.TestCase):
    """The explorer shows numbers of the article; the data file must carry them unchanged."""

    @classmethod
    def setUpClass(cls):
        cls.data = make_tool_data.build()

    def test_every_scenario_covers_all_weight_bands(self):
        for drug in self.data['drugs'].values():
            for table in drug['scenarios'].values():
                self.assertEqual(set(table), set(self.data['bands']))

    def test_values_of_the_article_table(self):
        main = self.data['drugs']['pembrolizumab']['scenarios']['main']
        self.assertAlmostEqual(main['>=150']['200 mg Q3W']['below'], 0.133, places=3)
        self.assertAlmostEqual(main['<50']['2 mg/kg Q3W']['below'], 0.069, places=3)
        nivolumab = self.data['drugs']['nivolumab']['scenarios']['main']
        self.assertAlmostEqual(nivolumab['>=150']['240 mg Q2W']['below'], 0.185, places=3)

    def test_fractions_are_proportions_and_band_counts_are_positive(self):
        for drug in self.data['drugs'].values():
            for table in drug['scenarios'].values():
                for band in table.values():
                    for cell in band.values():
                        for key in ('below', 'above', 'first'):
                            self.assertTrue(0 <= cell[key] <= 1)
                        self.assertGreater(cell['n'], 0)

    def test_source_hash_matches_the_zip(self):
        import hashlib
        self.assertEqual(self.data['source']['sha256'], hashlib.sha256(make_tool_data.ZIP.read_bytes()).hexdigest())


if __name__ == '__main__':
    unittest.main()
