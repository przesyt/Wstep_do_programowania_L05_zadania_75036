def wyswietl(*args):
    print(*args)
    return max(args)

print("Maksimum:", wyswietl(3, 8, 1, 5))