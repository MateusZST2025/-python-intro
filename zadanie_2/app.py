import re
from datetime import datetime

# Sprawdzenie poprawności adresu e-mail
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Obliczanie pola prostokąta
def rectangle_area(width, height):
    return width * height if width > 0 and height > 0 else None

# Filtrowanie listy (tylko liczby większe od 10)
def filter_numbers(lst):
    return [num for num in lst if num > 10]

# Konwersja daty (format: DD-MM-YYYY → YYYY/MM/DD)
def convert_date_format(date_str):
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y/%m/%d")
    except ValueError:
        return None

# Sprawdzenie, czy tekst to palindrom
def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]
