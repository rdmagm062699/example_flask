import unittest
import mock 
from src.data import get_all
from src.models import Data

class TestData(unittest.TestCase):

    @mock.patch('src.data.Data')
    def test_returns_empty_list_if_nothing_in_database(self, data_mock):
        data_mock.query.all.return_value = []
        self.assertEqual(get_all(), [])

    @mock.patch('src.data.Data')
    def test_returns_empty_list_if_nothing_in_database(self, data_mock):
        test_data = Data()
        test_data.id = 1
        test_data.data_value = "blah"

        data_mock.query.all.return_value = [test_data]
    
        expected = [test_data]

        self.assertEqual(get_all(), expected)
