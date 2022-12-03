from unittest import TestCase
from unittest.mock import patch

from game import describe_invalid_move
from game import WATER_TILE
from game import LAND_TILE
from game import ISLAND_TILE


class TestDescribeInvalidMove(TestCase):
    @patch('random.randint', return_value=2)
    def test_fishing(self, mock_randint):
        user_position = {'x-coordinate': 0, 'y-coordinate': 0, 'rod level': 0}
        simple_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): WATER_TILE, (1, 1): LAND_TILE}
        move = "fishing"
        expected_output = "I'll be surprised if you can reel in any fish here, seeing as there are no fish here."
        self.assertEqual(describe_invalid_move(simple_board, user_position, move), expected_output)

    @patch('random.randint', return_value=2)
    def test_invalid_water(self, mock_randint):
        user_position = {'x-coordinate': 1, 'y-coordinate': 0, 'rod level': 0}
        simple_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): WATER_TILE, (1, 1): LAND_TILE}
        move = "north"
        expected_output = "You look into the void.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe void looks back.\nYou should turn back"
        self.assertEqual(describe_invalid_move(simple_board, user_position, move), expected_output)
