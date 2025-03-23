import unittest
from zadanie_3_lib.data_utils import string_to_int, list_to_dict, average, is_valid_email, filter_positive_numbers, \
    DataProcessor


class TestDataUtils(unittest.TestCase):

    def test_string_to_int(self):
        self.assertEqual(string_to_int('123'), 123)
        self.assertRaises(ValueError, string_to_int, 'abc')

    def test_list_to_dict(self):
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        self.assertEqual(list_to_dict(keys, values), {'a': 1, 'b': 2, 'c': 3})
        self.assertRaises(ValueError, list_to_dict, keys, [1, 2])

    def test_average(self):
        self.assertEqual(average([1, 2, 3]), 2.0)
        self.assertRaises(ValueError, average, [])

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("test.com"))

    def test_filter_positive_numbers(self):
        self.assertEqual(filter_positive_numbers([1, -1, 2, -2]), [1, 2])

    def test_data_processor(self):
        processor = DataProcessor([3, 1, 2])
        self.assertEqual(processor.sort_data(), [1, 2, 3])
        self.assertEqual(processor.filter_even_numbers(), [2])


if __name__ == '__main__':
    unittest.main()
