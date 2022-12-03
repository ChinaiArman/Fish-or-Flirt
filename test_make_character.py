from unittest import TestCase
from unittest.mock import patch

from game import make_character


class TestMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=['chris'])
    @patch('dialogue.slow_print', side_effect=[''])
    def test_make_character_chris(self, mock_input, mock_slow_print):
        expected = {"name": 'chris', "x-coordinate": 9, "y-coordinate": 0, "luck": 40, "charisma": 40, "rod level": 0,
                    "xp": 0, "inventory": ["Mama's Fishing Rod"]}
        actual = make_character(10)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('dialogue.slow_print', side_effect=[''])
    def test_make_character_blank(self, mock_input, mock_slow_print):
        expected = {"name": '', "x-coordinate": 15, "y-coordinate": 0, "luck": 40, "charisma": 40, "rod level": 0,
                    "xp": 0, "inventory": ["Mama's Fishing Rod"]}
        actual = make_character(16)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['625'])
    @patch('dialogue.slow_print', side_effect=[''])
    def test_make_character_numbers(self, mock_input, mock_slow_print):
        expected = {"name": '625', "x-coordinate": 9, "y-coordinate": 0, "luck": 40, "charisma": 40, "rod level": 0,
                    "xp": 0, "inventory": ["Mama's Fishing Rod"]}
        actual = make_character(10)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6 whole rotisserie chicken'])
    @patch('dialogue.slow_print', side_effect=[''])
    def test_make_character_sentence(self, mock_input, mock_slow_print):
        expected = {"name": '6 whole rotisserie chicken', "x-coordinate": 9, "y-coordinate": 0, "luck": 40,
                    "charisma": 40, "rod level": 0, "xp": 0, "inventory": ["Mama's Fishing Rod"]}
        actual = make_character(10)
        self.assertEqual(expected, actual)
