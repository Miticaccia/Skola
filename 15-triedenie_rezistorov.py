pocet_rezistorov = int(input("Zadajte počet rezistorov: "))

rezistory = []
for i in range(pocet_rezistorov):
    x = int(input("Zadajte odpor rezistora: "))
    rezistory.append(x)

rezistory.sort()
print(rezistory)