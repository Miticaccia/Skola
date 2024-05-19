def delitel(a,b):
    while a != b:
        if a>b:
            a = a - b
        else:
            b = b - a
    return a 

cislo1 = int(input("Zadajte prvé číslo: "))
cislo2 = int(input("Zadajte druhé číslo: "))

if cislo1 == 0 or cislo2 == 0:
    print("Bola zadaná nulová hodnota!")
elif cislo1 < 0 or cislo2 <0:
    cislo1 = abs(cislo1)
    cislo2 = abs(cislo2)

d= delitel(cislo1,cislo2)
print("Najväčší spoločný deliteľ čísel", cislo1, "a", cislo2, "je číslo", d)