from unittest import TestCase

from game import LAND_TILE, WATER_TILE
from game import make_board


class TestMakeBoard(TestCase):
    def test_make_board_rows_columns_10(self):
        test_board = make_board(10, 10)
        expected = 100, LAND_TILE
        actual = len(test_board), test_board[9, 0]
        self.assertEqual(expected, actual)

    def test_make_board_rows_columns_16(self):
        test_board = make_board(16, 16)
        expected = 256, WATER_TILE
        actual = len(test_board), test_board[15, 0]
        self.assertEqual(expected, actual)
