from unittest import TestCase
from unittest.mock import patch

from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.print', side_effect=['', '', '', '', '', '', ''])
    @patch('builtins.input', side_effect=['1'])
    def test_user_input_1(self, mock_print, mock_input):
        expected = -1, 0
        actual = get_user_choice({"x-coordinate": 0, "y-coordinate": 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', '', '', '', '', ''])
    @patch('builtins.input', side_effect=['2'])
    def test_user_input_2(self, mock_print, mock_input):
        expected = 1, 0
        actual = get_user_choice({"x-coordinate": 0, "y-coordinate": 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', '', '', '', '', ''])
    @patch('builtins.input', side_effect=['3'])
    def test_user_input_3(self, mock_print, mock_input):
        expected = 0, 1
        actual = get_user_choice({"x-coordinate": 0, "y-coordinate": 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', '', '', '', '', ''])
    @patch('builtins.input', side_effect=['4'])
    def test_user_input_4(self, mock_print, mock_input):
        expected = 0, -1
        actual = get_user_choice({"x-coordinate": 0, "y-coordinate": 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', '', '', '', '', ''])
    @patch('builtins.input', side_effect=['5'])
    def test_user_input_5(self, mock_print, mock_input):
        expected = 'fishing'
        actual = get_user_choice({"x-coordinate": 0, "y-coordinate": 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', '', '', '', '', '', ''])
    @patch('builtins.input', side_effect=['6'])
    @patch('builtins.quit', side_effect=[''])
    def test_user_input_6(self, mock_print, mock_input, mock_quit):
        expected = None
        actual = get_user_choice({"x-coordinate": 0, "y-coordinate": 0})
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', '', '', '', '', '', ''])
    @patch('builtins.input', side_effect=['seven'])
    def test_user_input_non_option(self, mock_print, mock_input):
        expected = False
        actual = get_user_choice({"x-coordinate": 0, "y-coordinate": 0})
        self.assertEqual(expected, actual)
