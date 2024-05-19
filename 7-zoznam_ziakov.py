pocet = int(input("Koľko priezvísk chcete zoradiť? "))
ziaci = []
for i in range (pocet):
    x = str(input("Zadajte priezvisko: "))
    ziaci.append(x)

ziaci.sort()

print(ziaci)