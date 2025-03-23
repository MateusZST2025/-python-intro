import unittest
from zadanie_3_lib.text_processing import reverse_string, count_vowels, word_count, to_upper_case, remove_punctuation, word_frequency, sentence_count, capitalize_first_letter, TextManipulator

class TestTextProcessing(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello'), 2)

    def test_word_count(self):
        self.assertEqual(word_count('hello world'), 2)

    def test_to_upper_case(self):
        self.assertEqual(to_upper_case('hello'), 'HELLO')

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation('hello, world!'), 'hello world')

    def test_word_frequency(self):
        self.assertEqual(word_frequency('hello hello world'), {'hello': 2, 'world': 1})

    def test_sentence_count(self):
        self.assertEqual(sentence_count('Hello. How are you?'), 2)

    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize_first_letter('hello world'), 'Hello World')

    def test_text_manipulator(self):
        manipulator = TextManipulator("hello hello world")
        self.assertEqual(manipulator.get_word_count(), 3)
        self.assertEqual(manipulator.get_vowel_count(), 5)
        self.assertEqual(manipulator.get_word_frequency(), {'hello': 2, 'world': 1})

if __name__ == '__main__':
    unittest.main()
