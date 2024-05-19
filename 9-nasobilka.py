import random

def nasobenie(a,b):
    print(a, "*", b, "=")
    vysledok = int(input("Napíšte výsledok príkladu: "))
    spravne = a * b
    if vysledok == spravne:
        print("Správne!")
    else:
        print("Zle! Správny výsleodk je: ", spravne)

cislo1 = int(input("Zadajte prvé číslo: "))
cislo2 = int(input("Zadajte druhé číslo: "))
nasobenie(cislo1,cislo2)

dalsi = True
while dalsi:
   odpoved = str(input("Chcete dalsi príklad?(y/n) "))
   if odpoved == "y" or odpoved == "Y":
       prve_cislo = random.randint(0,10)
       druhe_cislo = random.randint(0,10)
       nasobenie(prve_cislo,druhe_cislo)
   else:
       dalsi = False