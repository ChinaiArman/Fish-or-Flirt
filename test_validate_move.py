from unittest import TestCase

from game import LAND_TILE, WATER_TILE
from game import validate_move


class TestValidateMove(TestCase):
    def test_direction_false(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 0, 'y-coordinate': 0}
        test_direction = False
        expected = (0, 0), False
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_fishing_false(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 0, 'y-coordinate': 0, 'rod level': 0}
        test_direction = 'fishing'
        expected = 'fishing', False
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_fishing_true(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): LAND_TILE, (1, 1): WATER_TILE}
        test_character = {'x-coordinate': 1, 'y-coordinate': 0, 'rod level': 0}
        test_direction = 'fishing'
        expected = 'fishing', True
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_x_direction_false(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 0, 'y-coordinate': 0}
        test_direction = (0, -1)
        expected = (0, 0), False
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_x_direction_true(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 0, 'y-coordinate': 0}
        test_direction = (0, 1)
        expected = (0, 1), True
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_y_direction_false(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 1, 'y-coordinate': 1}
        test_direction = (2, 1)
        expected = (1, 1), False
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_y_direction_true(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 1, 'y-coordinate': 1}
        test_direction = (0, 1)
        expected = (0, 1), True
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_move_onto_water_false(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): WATER_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 0, 'y-coordinate': 0, 'rod level': 0}
        test_direction = (0, 1)
        expected = (0, 0), False
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)

    def test_move_onto_water_true(self):
        test_board = {(0, 0): LAND_TILE, (0, 1): WATER_TILE, (1, 0): LAND_TILE, (1, 1): LAND_TILE}
        test_character = {'x-coordinate': 0, 'y-coordinate': 0, 'rod level': 1}
        test_direction = (0, 1)
        expected = (0, 1), True
        actual = validate_move(test_board, test_character, test_direction, 2, 2)
        self.assertEqual(expected, actual)
