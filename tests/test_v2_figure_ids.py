import unittest

from scripts.v2_validate import valid_figure_id


class FigureIdNamespaceTests(unittest.TestCase):
    def test_standard_namespace(self):
        self.assertTrue(valid_figure_id("CH02", "CH02-FIG-123"))

    def test_ch01_homage_namespace(self):
        self.assertTrue(valid_figure_id("CH01", "CH01-HOMAGE-FIG-001"))

    def test_homage_namespace_is_ch01_only(self):
        self.assertFalse(valid_figure_id("CH02", "CH01-HOMAGE-FIG-001"))

    def test_malformed_ids_are_rejected(self):
        self.assertFalse(valid_figure_id("CH01", "CH01-HOMAGE-FIG-1"))
        self.assertFalse(valid_figure_id("CH01", "CH01-FIG-001-extra"))


if __name__ == "__main__":
    unittest.main()
