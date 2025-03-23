import unittest
from app import is_valid_email, rectangle_area, filter_numbers, convert_date_format, is_palindrome

class TestFunctions(unittest.TestCase):

    def setUp(self):
        """ Przygotowanie wspólnych danych dla testów """
        self.valid_email = "test@example.com"
        self.invalid_email = "test.com"
        self.rectangles = [(5, 4, 20), (0, 5, None), (-1, 4, None)]
        self.lists = [[5, 15, 20, 8], [10, 9, 8], []]

    def test_valid_email(self):
        self.assertTrue(is_valid_email(self.valid_email))
        self.assertFalse(is_valid_email(self.invalid_email))

    def test_rectangle_area(self):
        for width, height, expected in self.rectangles:
            self.assertEqual(rectangle_area(width, height), expected)

    def test_filter_numbers(self):
        self.assertEqual(filter_numbers([5, 15, 20, 8]), [15, 20])
        self.assertEqual(filter_numbers([1, 2, 3]), [])
        self.assertEqual(filter_numbers([10, 11, 12]), [11, 12])

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("25-12-2023"), "2023/12/25")
        self.assertIsNone(convert_date_format("31-02-2023"))
        self.assertEqual(convert_date_format("01-01-2000"), "2000/01/01")

    def test_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))
        self.assertFalse(is_palindrome("python"))
        self.assertTrue(is_palindrome("madam"))

    def test_filter_numbers_extra(self):
        self.assertEqual(filter_numbers([]), [])  # Pusta lista
        self.assertEqual(filter_numbers([10, 9, 8, 7]), [])  # Wszystkie liczby <10
        self.assertEqual(filter_numbers([100, 50, 11]), [100, 50, 11])  # Wszystkie liczby >10

    def test_convert_date_format_extra(self):
        self.assertIsNone(convert_date_format(""))  # Pusty string
        self.assertIsNone(convert_date_format("31/12/2023"))  # Zły format
        self.assertEqual(convert_date_format("29-02-2024"), "2024/02/29")  # Rok przestępny

    def test_palindrome_extra(self):
        self.assertTrue(is_palindrome(""))  # Pusty string powinien być palindromem
        self.assertTrue(is_palindrome("a"))  # Pojedyncza litera to palindrom
        self.assertFalse(is_palindrome("Test"))  # Losowy tekst niebędący palindromem

if __name__ == "__main__":
    unittest.main()
