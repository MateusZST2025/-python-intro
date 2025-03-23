def reverse_string(text: str) -> str:
    """Odwraca ciąg znaków."""
    return text[::-1]


def count_vowels(text: str) -> int:
    """Zlicza samogłoski w ciągu znaków."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


def word_count(text: str) -> int:
    """Zlicza liczbę słów w tekście."""
    words = text.split()
    return len(words)


def to_upper_case(text: str) -> str:
    """Zmienia wszystkie litery na wielkie."""
    return text.upper()


def remove_punctuation(text: str) -> str:
    """Usuwa wszystkie znaki interpunkcyjne z tekstu."""
    return ''.join(char for char in text if char.isalnum() or char.isspace())


def word_frequency(text: str) -> dict:
    """Zlicza częstotliwość występowania słów w tekście."""
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def sentence_count(text: str) -> int:
    """Zlicza liczbę zdań w tekście."""
    sentences = text.split('.')
    return len([s for s in sentences if s.strip()])


def capitalize_first_letter(text: str) -> str:
    """Zmienia pierwszą literę w każdym słowie na wielką."""
    return ' '.join([word.capitalize() for word in text.split()])


class TextManipulator:
    """Klasa do manipulacji tekstem."""

    def __init__(self, text: str):
        self.text = text

    def get_word_count(self) -> int:
        """Zwraca liczbę słów w tekście."""
        return len(self.text.split())

    def get_vowel_count(self) -> int:
        """Zwraca liczbę samogłosk w tekście."""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in self.text if char in vowels)

    def get_word_frequency(self) -> dict:
        """Zlicza częstotliwość słów w tekście."""
        words = self.text.lower().split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        return freq
