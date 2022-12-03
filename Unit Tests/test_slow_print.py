import io
import unittest.mock
from unittest import TestCase
from dialogue import slow_print


class TestSlowPrint(TestCase):
    @unittest.mock.patch('dialogue.sleep', return_value=None)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_string(self, patched_sleep, mock_output):
        slow_print("Hello World")
        printed_statement = mock_output.getValue()
        expected = "Hello World.\n"
        self.assertEqual(printed_statement, expected)
