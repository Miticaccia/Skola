def triedenie(list1, list2):
    for i in range(len(list2) - 1):
        for j in range(len(list2) - i - 1):
            if list2[j] < list2[j+1]:
                temp1 = list2[j]
                temp2 = list1[j]
                list2[j] = list2[j+1]
                list1[j] = list1[j+1]
                list2[j+1] = temp1
                list1[j+1] = temp2
    return list2


ziaci = []
vysky = []
pocet_ziakov = int(input("Zadajte počet žiakov: "))

for i in range(pocet_ziakov):
    x = str(input("Napíšte meno žiaka: "))
    ziaci.append(x)
    y = int(input("Zdajte výšku tohto žiaka: "))
    vysky.append(y)
print("Neutriedene pole žiakov: ", ziaci)
print("Neutriedene pole výšok: ", vysky)
print("---------------------")
triedenie(ziaci,vysky)
print("Utriedený zoznam žiakov a výšok je:")
print(ziaci)
print(vysky) 