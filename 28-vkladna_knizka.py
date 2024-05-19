p = int(input("Zadajte úrok: "))
ciastka = int(input("Zadajte čiastku: "))

suma = 0
for i in range(0,10):
    suma = suma * (1+p/100) + 500
print("Za 10 rokov sa našporilo ", suma, "€.")

suma = 0
rok = 0
while suma <= ciastka:
    suma = suma * (1+p/100) + 500
    rok += 1
print("Uspery prekrocia  ciastku za: ", rok, "rokov.")