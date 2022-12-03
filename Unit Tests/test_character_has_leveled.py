from unittest import TestCase
from game import character_has_leveled


class TestCharacterHasLeveled(TestCase):
    def test_xp_and_rod_equal(self):
        expected = False
        actual = character_has_leveled({'xp': 1, 'rod level': 1})
        self.assertEqual(expected, actual)

    def test_xp_greater(self):
        expected = True
        actual = character_has_leveled({'xp': 1, 'rod level': 0})
        self.assertEqual(expected, actual)
