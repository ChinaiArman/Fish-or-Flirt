import io
import unittest.mock
import time
from unittest import TestCase
from dialogue import loading


class TestLoading(TestCase):
    @unittest.mock.patch('time.sleep', return_value=None)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_one_instance(self):
        self.assertEqual()
