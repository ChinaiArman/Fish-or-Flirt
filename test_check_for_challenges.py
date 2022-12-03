from unittest import TestCase
from unittest.mock import patch

import events
from game import WATER_TILE, LAND_TILE, BOAT_TILE, SKULL_TILE, LEVIATHAN_TILE, ISLAND_TILE
import dialogue
from game import check_for_challenges


class TestCheckForChallenges(TestCase):
    def test_check_for_boat_event(self):
        expected = True, events.boat_event, dialogue.BOAT_DIALOGUE
        actual = check_for_challenges({(0, 0): BOAT_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    def test_check_for_pirate_event(self):
        expected = True, events.pirate_event, dialogue.PIRATE_DIALOGUE
        actual = check_for_challenges({(0, 0): SKULL_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    def test_check_for_leviathan_event(self):
        expected = True, events.leviathan_event, dialogue.LEVIATHAN_DIALOGUE
        actual = check_for_challenges({(0, 0): LEVIATHAN_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[16])
    def test_check_for_crab_event(self, mock_randint):
        expected = True, events.land_event, dialogue.CRAB_DIALOGUE
        actual = check_for_challenges({(0, 0): LAND_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[20])
    def test_check_for_fisherman_event(self, mock_randint):
        expected = True, events.land_event, dialogue.FISHERMAN_DIALOGUE
        actual = check_for_challenges({(0, 0): LAND_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[16])
    def test_check_for_mermaid_event(self, mock_randint):
        expected = True, events.water_event, dialogue.MERMAID_DIALOGUE
        actual = check_for_challenges({(0, 0): WATER_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[20])
    def test_check_for_whale_event(self, mock_randint):
        expected = True, events.water_event, dialogue.WHALE_DIALOGUE
        actual = check_for_challenges({(0, 0): WATER_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[40, 0])
    @patch('builtins.print', side_effect=[''])
    def test_no_land_event(self, mock_randint, mock_print):
        expected = False, None, None
        actual = check_for_challenges({(0, 0): LAND_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[40, 0])
    @patch('builtins.print', side_effect=[''])
    def test_no_water_event(self, mock_randint, mock_print):
        expected = False, None, None
        actual = check_for_challenges({(0, 0): WATER_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=[''])
    def test_island_tile(self, mock_print):
        expected = False, None, None
        actual = check_for_challenges({(0, 0): ISLAND_TILE}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=[''])
    def test_catch_all(self, mock_print):
        expected = False, None, None
        actual = check_for_challenges({(0, 0): 'banana'}, {'x-coordinate': 0, 'y-coordinate': 0})
        self.assertEqual(expected, actual)
