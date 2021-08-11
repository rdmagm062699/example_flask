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
        test_data.data_value = 'blah'

        data_mock.query.all.return_value = [test_data]
    
        expected = [test_data]

        self.assertEqual(get_all(), expected)

    @mock.patch('src.data.Data')
    def test_returns_only_numeric_values_if_instructed_to_do_so(self, data_mock):
        test_data1 = Data()
        test_data1.id = 1
        test_data1.data_value = "not_number"
        
        test_data2 = Data()
        test_data2.id = 2
        test_data2.data_value = "2"

        data_mock.query.all.return_value = [test_data1, test_data2]

        expected_data = Data()
        expected_data.id = 2
        expected_data.data_value = "2"
        
        expected = [expected_data]

        self.assertEqual(get_all('only_numbers'), expected)
