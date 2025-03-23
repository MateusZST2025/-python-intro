def add_numbers(a: float, b: float) -> float:
    """Zwraca sumę dwóch liczb."""
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """Zwraca iloczyn dwóch liczb."""
    return a * b

def factorial(n: int) -> int:
    """Oblicza silnię z liczby n."""
    if n < 0:
        raise ValueError("Liczba musi być nieujemna.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """Zwraca n-ty element ciągu Fibonacciego."""
    if n <= 0:
        raise ValueError("N musi być liczbą całkowitą dodatnią.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def power(base: float, exponent: int) -> float:
    """Zwraca podstawę podniesioną do określonej potęgi."""
    return base ** exponent

def square_root(x: float) -> float:
    """Zwraca pierwiastek kwadratowy z liczby."""
    if x < 0:
        raise ValueError("Pierwiastek kwadratowy z liczby ujemnej nie istnieje.")
    return x ** 0.5

def matrix_multiply(A: list, B: list) -> list:
    """Mnoży dwie macierze (A i B)."""
    if len(A[0]) != len(B):
        raise ValueError("Nie można pomnożyć macierzy. Liczba kolumn A musi być równa liczbie wierszy B.")
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

class MathOperations:
    """Klasa z operacjami matematycznymi."""
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def square_root(x: float) -> float:
        if x < 0:
            raise ValueError("Pierwiastek kwadratowy z liczby ujemnej nie istnieje.")
        return x ** 0.5
