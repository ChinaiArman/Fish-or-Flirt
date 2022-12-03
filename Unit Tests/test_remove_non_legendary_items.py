from unittest import TestCase
from game import remove_non_legendary_items


class TestRemoveNonLegendaryItems(TestCase):
    def test_non_legendary(self):
        expected = False
        actual = remove_non_legendary_items("Fishies")
        self.assertEqual(expected, actual)

    def test_legendary_item(self):
        expected = True
        actual = remove_non_legendary_items("An Unspoken Level of Rod-ly-ness")
        self.assertEqual(expected, actual)
