def string_to_int(value: str) -> int:
    """Konwertuje stringa na liczbę całkowitą."""
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Nie można przekonwertować {value} na liczbę.")


def list_to_dict(keys: list, values: list) -> dict:
    """Konwertuje dwie listy na słownik."""
    if len(keys) != len(values):
        raise ValueError("Listy muszą mieć tę samą długość.")
    return dict(zip(keys, values))


def average(numbers: list) -> float:
    """Zwraca średnią wartość z listy liczb."""
    if not numbers:
        raise ValueError("Lista nie może być pusta.")
    return sum(numbers) / len(numbers)


def is_valid_email(email: str) -> bool:
    """Sprawdza, czy adres e-mail jest poprawny."""
    return '@' in email and '.' in email


def filter_positive_numbers(numbers: list) -> list:
    """Filtruje tylko dodatnie liczby z listy."""
    return [num for num in numbers if num > 0]


class DataProcessor:
    """Klasa do przetwarzania danych."""

    def __init__(self, data: list):
        self.data = data

    def sort_data(self) -> list:
        """Sortuje dane rosnąco."""
        return sorted(self.data)

    def filter_even_numbers(self) -> list:
        """Filtruje liczby parzyste z danych."""
        return [num for num in self.data if num % 2 == 0]
