from unittest import TestCase
from game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_has_leviathan(self):
        expected = True
        actual = check_if_goal_attained({'inventory': ["fishie", "stick", "stick", "Leviathan"]})
        self.assertEqual(expected, actual)

    def test_no_leviathan(self):
        expected = False
        actual = check_if_goal_attained({'inventory': ['boot', 'mermaid']})
        self.assertEqual(expected, actual)

    def test_empty_inventory(self):
        expected = False
        actual = check_if_goal_attained({'inventory': []})
        self.assertEqual(expected, actual)
