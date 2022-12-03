from unittest import TestCase
from game import remove_non_legendary_items


class TestRemoveNonLegendaryItems(TestCase):
    def test_non_legendary(self):
        self.assertEqual(remove_non_legendary_items("Fishies"), False)

    def test_legendary_item(self):
        self.assertEqual(remove_non_legendary_items("An Unspoken Level of Rod-ly-ness"), True)
