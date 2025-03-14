#import modułu random
import random

#stoworzone dwie listy
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

#łączymy listy za pomocą zip()
polaczone = list(zip(lista1, lista2))
print("Połączone listy:", polaczone)

#funkcja z modułu random
losowa_liczba = random.randint(1, 10)
print("Losowa liczba:", losowa_liczba)

#obsługa wyjątku try-except.
try:
    wynik = 10 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")

#dokumentacja:
#zip(): https://docs.python.org/3/library/functions.html#zip
#random.randint(): https://docs.python.org/3/library/random.html#random.randint
#ZeroDivisionError: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
