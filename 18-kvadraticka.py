import math
dalsi = True
while dalsi:
    print("Kvadratická rovnica je daná predpisom ax\u00b2 + bx + c = 0")
    a = float(input("Zadajte parameter a: "))
    b = float(input("Zadajte parameter b: "))
    c = float(input("Zadajte parameter c: "))

    if a == 0:
        print("Parameter a sa nemôže rovnať nule!")
        break

    D = b * b - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Korene rovnice sú x1 = ", x1, "x2 = ", x2)
    elif D == 0:
        x1 = -b / (2 * a)
        print("Koreň rovnice je x1 = ", x1)
    else:
        print("Rovnica nemá reálne korene.")
    odpoved = str(input("Chcete zadať ďalšie parametre?(y/n) "))
    if odpoved == "y" or odpoved == "Y":
        dalsi = True
    else: 
        dalsi = False