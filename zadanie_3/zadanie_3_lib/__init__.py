# Importowanie funkcji z modułów
from .data_utils import string_to_int, list_to_dict, average, is_valid_email, filter_positive_numbers
from .math_tools import add_numbers, multiply_numbers, factorial, fibonacci, power, square_root, matrix_multiply
from .text_processing import reverse_string, count_vowels, word_count, to_upper_case, remove_punctuation, word_frequency, sentence_count, capitalize_first_letter

# Udostępnianie klas z modułów
from .data_utils import DataProcessor
from .math_tools import MathOperations
from .text_processing import TextManipulator

# Funkcja inicjalizacyjna
def init_config():
    print("Pakiet zainicjowany!")

# Możesz dodać zmienne globalne lub konfigurację, jeśli chcesz
__version__ = "1.0.0"
author = "Mateusz Gruszczynski"