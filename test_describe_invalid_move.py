from unittest import TestCase
from unittest.mock import patch

from game import describe_invalid_move
from game import WATER_TILE
from game import LAND_TILE
from game import ISLAND_TILE


class TestDescribeInvalidMove(TestCase):
    @patch('game.randint', side_effect=[2])
    def test_fishing(self, mock_random):
        user_position = {'x-coordinate': 0, 'y-coordinate': 0, 'rod level': 0}
        simple_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): WATER_TILE, (1, 1): LAND_TILE}
        move = "fishing"
        expected = "I'll be surprised if you can reel in any fish here, seeing as there are no fish here."
        actual = describe_invalid_move(simple_board, user_position, move)
        self.assertEqual(actual, expected)

    @patch('game.randint', side_effect=[1])
    def test_invalid_water(self, mock_random):
        user_position = {'x-coordinate': 1, 'y-coordinate': 0, 'rod level': 0}
        simple_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): WATER_TILE, (1, 1): LAND_TILE}
        move = "north"
        expected = "You look into the void.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe void " \
                   "looks back.\nYou should turn back"
        actual = describe_invalid_move(simple_board, user_position, move)
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[2])
    def test_invalid_land(self, mock_random):
        user_position = {'x-coordinate': 0, 'y-coordinate': 0, 'rod level': 0}
        simple_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): WATER_TILE, (1, 1): LAND_TILE}
        move = "east"
        expected = "The crabs look at you with disgust. What are you, stupid? You can't go there! Go somewhere else!"
        actual = describe_invalid_move(simple_board, user_position, move)
        self.assertEqual(expected, actual)

    @patch('game.randint', side_effect=[1])
    def test_invalid_island(self, mock_random):
        user_position = {'x-coordinate': 1, 'y-coordinate': 1, 'rod level': 0}
        simple_board = {(0, 0): ISLAND_TILE, (0, 1): LAND_TILE, (1, 0): WATER_TILE, (1, 1): ISLAND_TILE}
        move = "east"
        expected = "Let's review our NUMBERS. 1 for NORTH. 2 for SOUTH. 3 for EAST. 4 for SOUTH. Try again."
        actual = describe_invalid_move(simple_board, user_position, move)
        self.assertEqual(expected, actual)
