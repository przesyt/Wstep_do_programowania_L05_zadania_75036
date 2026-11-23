def wskaznik_BMI(waga, wzrost):
    BMI = waga / (wzrost**2) * 10000
    BMI = round(BMI, 2)
    if BMI < 18.5:
        print(f"BMI wynosi {BMI}, niedowaga")
    elif BMI < 25:
        print(f"BMI wynosi {BMI}, pożądana masa ciała")
    elif BMI < 30:
        print(f"BMI wynosi {BMI}, nadwaga")
    elif BMI < 35:
        print(f"BMI wynosi {BMI}, otyłość I stopnia")
    elif BMI < 40:
        print(f"BMI wynosi {BMI}, otyłość II stopnia")
    else:
        print(f"BMI wynosi {BMI}, otyłość III stopnia")
    return BMI


waga = float(input("Podaj wagę (kg): "))
wzrost = float(input("Podaj wzrost (cm): "))
wskaznik_BMI(waga, wzrost)