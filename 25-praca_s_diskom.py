temp1 = open ("priezviska.txt", "r")
priezviska = []
počet = 0
riadok1 = temp1.readline()
while riadok1 != "":
    priezviska.append(riadok1.strip())
    riadok1 = temp1.readline()
    počet += 1
print("V súbore je ", počet, "mien.")
temp1.close()

nenachadza = False
meno = input("Zadajte hľadané meno: ")
for i in range(len(priezviska)):
    if meno == priezviska[i]:
        print("Zadané meno sa nachádza v zozname.")
        nenachadza = False
        break
    else:
        nenachadza = True
if nenachadza == True:
    print("Zadane meno sa nenachádza v zozname.")
