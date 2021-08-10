import unittest
import mock 
from src.data import get_all

class TestData(unittest.TestCase):

    @mock.patch('src.data.Data')
    def test_returns_empty_list_if_nothing_in_database(self, data_mock):
        self.assertEqual(get_all(), [])