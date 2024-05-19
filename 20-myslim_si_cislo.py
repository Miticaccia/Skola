import random
dalsi = True
while dalsi:
    print("Vymyslím si číslo. Napíš v akom rozsahu!")
    od = int(input("Napíš začiatok intervalu: "))
    do = int(input("Napíš koniec intervalu: "))
    hladane_cislo = random.randint(od,do)

    neuhadol = True
    while neuhadol:
        hadaj = int(input("Hádaj moje číslo: "))
        if hadaj == hladane_cislo:
            print("Gratulujem! Uhádol si moje číslo!")
            neuhadol = False
        elif hadaj > hladane_cislo:
            print("Neuhádol si! Skús menšie číslo.")
            neuhadol = True
        else:
            print("Nauhadol si! Skús väčšie číslo.")
            neuhadol = True

    odpoved = str(input("Chceš hádať znova?(y/n) "))
    if odpoved == "y" or odpoved == "Y":
        dalsi = True
    else:
        dalsi = False