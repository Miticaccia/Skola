def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range (2, cislo-1):
        if cislo % i == 0:
            return False
    return True

while True:
    cislo = int(input("Zadajte prirodzené číslo väčšie ako 1: "))
    if cislo <= 1:
        print("Zadané číslo je menšie alebo rovné 1.")
    elif je_prvocislo(cislo):
        print ("Zadané číslo je prvošíslo!")
    else:
        print("Zadané číslo nie je prvočíslo!")