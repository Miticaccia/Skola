dalsi = True
while dalsi == True:
    cislo1 = int(input("Zadajte prvé číslo príkladu: "))
    cislo2 = int(input("Zadajte druhé číslo prikladu: "))
    operacia = str(input("Akú matematickú operáciu chcete vykonať? (+,-,*,/): "))

    if operacia == "+":
        print("Súčet čísel ", cislo1, " a ", cislo2, " je ", cislo1 + cislo2)
    elif operacia == "-":
            print("Rozdiel čísel ", cislo1, " a ", cislo2, " je ", cislo1 - cislo2)
    elif operacia == "*":
            print("Súčin čísel ", cislo1, " a ", cislo2, " je ", cislo1 * cislo2)
    elif operacia == "/":
            print("Podiel čísel ", cislo1, " a ", cislo2, " je ", cislo1 / cislo2)
    odpoved = str(input("Chcete dalsi príklad? (y/n): "))
    if odpoved == "y":
          dalsi == True
    else:
          dalsi = False