import io
import unittest.mock
from unittest import TestCase
from dialogue import slow_print


class TestSlowPrint(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_string(self, mock_stdout):
        test_dialogue = "This is a string to test a function."
        slow_print(test_dialogue)
        printed_statement = mock_stdout.getValue()
        expected = "This is a string to test a function.\n"
        self.assertEqual(printed_statement, expected)
