from unittest import TestCase
from game import character_has_leveled


class TestCharacterHasLeveled(TestCase):
    def test_xp_and_rod_equal(self):
        character_level_stats_equal = {'xp': 1, 'rod level': 1}
        self.assertEqual(character_has_leveled(character_level_stats_equal), False)

    def test_xp_greater(self):
        character_stats_xp_greater = {'xp': 1, 'rod level': 0}
        self.assertEqual(character_has_leveled(character_stats_xp_greater), True)
