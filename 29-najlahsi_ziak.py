a = float(input("Zadajte hmotnosť žiaka: "))
for i in range(3):
    b = float(input("Zadajte hmotnosť žiaka: "))
    if b < a:
        a = b

print("Najľahší žiak má ", a, " kg.")