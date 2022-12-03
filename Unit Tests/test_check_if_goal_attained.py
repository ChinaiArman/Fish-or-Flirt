from unittest import TestCase
from game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_has_leviathan(self):
        inventory_with_leviathan = {'inventory': ["fishie", "stick", "stick", "Leviathan"]}
        self.assertEqual(check_if_goal_attained(inventory_with_leviathan), True)

    def test_no_leviathan(self):
        inventory_without_leviathan = {'inventory': ['boot', 'mermaid']}
        self.assertEqual(check_if_goal_attained(inventory_without_leviathan), False)

    def test_empty_inventory(self):
        empty_inventory = {'inventory': []}
        self.assertEqual(check_if_goal_attained(empty_inventory), False)
