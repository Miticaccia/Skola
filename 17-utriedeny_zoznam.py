ziaci = ["Richard", "Matej", "Alojz", "Martin", "Bruno"]
ziaci.sort()
hladane_meno = input("Zadajte hľadané meno: ")
meno = True

for i in range(len(ziaci)):
    if hladane_meno == ziaci[i]:
        print("Hladane priezvisko ", hladane_meno, " je v zozname.")
        break

    else:
        meno == False

if meno == False:
    print("Hladane priezvisko ", hladane_meno, " nie je v zozname.")