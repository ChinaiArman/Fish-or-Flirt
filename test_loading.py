from unittest import TestCase
import io
import unittest.mock

from dialogue import loading


class TestLoading(TestCase):
    @unittest.mock.patch('time.sleep', return_value=None)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_one_instance(self, patched_sleep, mock_output):
        loading(1)
        program_output = mock_output.getValue()
        expected_output = "...\n\n"
        self.assertEqual(program_output, expected_output)
