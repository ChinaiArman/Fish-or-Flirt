import io
import unittest.mock
import time
from unittest import TestCase
from dialogue import loading


class TestLoading(TestCase):
    @unittest.patch('time.sleep', return_value=None)
    def test_loading(self):
        self.fail()
