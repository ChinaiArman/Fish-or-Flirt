from unittest import TestCase

from game import scoring


class TestScoring(TestCase):
    def test_scored_item(self):
        expected = ('Shark', 3, 60)
        actual = scoring('Shark', 3)
        self.assertEqual(expected, actual)

    def test_item_not_scored(self):
        expected = ('banana', 5, 0)
        actual = scoring('banana', 5)
        self.assertEqual(expected, actual)
