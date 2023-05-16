# Dzień 84 - Liczby zmiennoprzecinkowe
# Funkcja print() - formatowanie liczb

number = 7
print("Moja ulubiona liczba to", liczba)

# str.format - pozwala na tworzenie szablonu łańcucha znaków z miejscami zastępczymi (w nawiasach klamrowych {}), które zostaną zastąpione wartościami podanymi jako argumenty
number1 = 3.14159
number2 = 42
text = "Liczba pi to {:.2f}, a odpowiedź na pytanie o życie, wszechświat i całą resztę to {}."
print(text.format(number1, number2))

# Formatowanie za pomocą f - stringów
number1 = 10
number2 = 20
print(f"Suma {number1} i {number2} wynosi {number1 + number2}.")

# Kontrola liczb miejsc po przecinku
number_pi = 3.1415926535
print(f"Liczba pi zaokrąglona do 3 miejsc po przecinku: {number_pi:.3f}")

# Zadanie:
(r) = 5
number_pi = 3.1415926535
print("(r)")

import math
print(math.pow(5,2))

print(f"Suma {number_pi} i {math.pow} wynosi {number_pi + mat.pow}.")

number1 = 3.14159
number2 = 25
text = "Wynik z pola powierzchni koła wynosi {:.2f}, odpowiedź to {}."
print(text.format(number1, number2))
