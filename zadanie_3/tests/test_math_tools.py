import unittest
from zadanie_3_lib.math_tools import add_numbers, multiply_numbers, factorial, fibonacci, power, square_root, \
    matrix_multiply, MathOperations


class TestMathTools(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertRaises(ValueError, factorial, -1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 3)
        self.assertRaises(ValueError, fibonacci, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertRaises(ValueError, square_root, -1)

    def test_matrix_multiply(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        self.assertEqual(matrix_multiply(A, B), [[19, 22], [43, 50]])

    def test_math_operations(self):
        self.assertEqual(MathOperations.add(2, 3), 5)
        self.assertEqual(MathOperations.multiply(2, 3), 6)
        self.assertEqual(MathOperations.square_root(16), 4)


if __name__ == '__main__':
    unittest.main()
