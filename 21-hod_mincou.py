import random
minca = ["znak", "číslo"]
pocty = [0,0]

for i in range(100):
    hod = random.randint(1,2)
    pocty[hod-1] += 1

print(minca)
print(pocty)

for i in range(2):
    print ("vyskyt javu", minca[i], pocty[i], "-krát.")