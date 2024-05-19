temp1 = open ("priezviska.txt","w")
pocet_priezvisok = int(input("Koľko priezvisok chcete zadať? "))
for i in range(pocet_priezvisok):
    priezvisko = input("Zadaj priezvisko: ")
    temp1.write(priezvisko+"\n")
temp1.close()

hladaj = input("Zadaj začiatočné písmeno: ")
hladane_priezviska = []
najdene_priezviska = []

temp2 = open("priezviska.txt", "r")
riadok1 = temp2.readline()
while riadok1 != "":
    hladane_priezviska.append(riadok1.strip())
    riadok1 = temp2.readline()
for j in range(len(hladane_priezviska)):
    if hladane_priezviska[j][0] == hladaj:
        najdene_priezviska.append(hladane_priezviska[j])

print("Všetky najdene priezviska su: ", najdene_priezviska)
temp2.close()