import random
cisla_kocky = [0]*6
hodnoty = ["1", "2", "3", "4", "5", "6"]
pocet_hodov = int(input("Koĺkokárt budeme hádzať kockou? "))

for a in range(0,pocet_hodov):
    hod = random.randint(1,6)
    cisla_kocky[hod - 1] += 1

print(cisla_kocky)
for i in range(0,6):
    print("Výskyt čísla", hodnoty[i]," bol ", cisla_kocky[i], "- krát!")