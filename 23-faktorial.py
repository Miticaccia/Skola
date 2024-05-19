sucin = 1
for i in range(1,10):
    sucin = sucin * i
        
print("Súčin čísel od 1 do 10 je: ", sucin)
print("\n")
cislo = int(input("Zadajte číslo hľadaného faktorialu: "))

faktorial = 1
for a in range(1,cislo + 1):
    faktorial = faktorial * a

print(cislo,"! = ", faktorial)