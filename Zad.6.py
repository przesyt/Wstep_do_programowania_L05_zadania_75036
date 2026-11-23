import math

def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Boki muszą być dodatnie.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("To nie jest trójkąt.")
    else:
        s = (a + b + c) / 2
        pole = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print("Pole:", pole)

try:
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    pole_trojkata(a, b, c)
except ValueError:
    print("Błąd: podaj liczby.")