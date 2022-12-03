from unittest import TestCase
from unittest.mock import patch

from game import execute_glow_up_protocol


class TestExecuteGlowUpProtocol(TestCase):
    @patch('builtins.print', side_effect=['', '', ''])
    def test_glow_up_charisma_luck_equal(self, mock_print):
        character_information = {'xp': 1, 'rod level': 0, 'charisma': 0, 'luck': 0}
        execute_glow_up_protocol(character_information)
        expected = {'xp': 1, 'rod level': 1, 'charisma': 2, 'luck': 2}
        actual = character_information
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', ''])
    def test_glow_up_charisma_greater(self, mock_print):
        character_information = {'xp': 2, 'rod level': 1, 'charisma': 2, 'luck': 0}
        execute_glow_up_protocol(character_information)
        expected = {'xp': 2, 'rod level': 2, 'charisma': 4, 'luck': 2}
        actual = character_information
        self.assertEqual(expected, actual)

    @patch('builtins.print', side_effect=['', '', ''])
    def test_glow_up_luck_greater(self, mock_print):
        character_information = {'xp': 2, 'rod level': 1, 'charisma': 4, 'luck': 37}
        execute_glow_up_protocol(character_information)
        expected = {'xp': 2, 'rod level': 2, 'charisma': 6, 'luck': 39}
        actual = character_information
        self.assertEqual(expected, actual)
