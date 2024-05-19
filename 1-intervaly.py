a = int(input("Zadajte začiatok prvého intervalu: "))
b = int(input("Zadajte koniec prvého intervalu: "))
c = int(input("Zadajte začiatok druhého intervalu: "))
d = int(input("Zadajte koniec druhého intervalu: "))
print("------------------------------")

if c > a and c < b:
    if d >= a and d <= b:
        print("Druhý interval je podmnožinou prvého intervalu!")
    else:
        print("Prienikom intervalov je interval (", c, ",", b)
elif d > a and d < b:
    if c >=a and c <= b:
        print("Druhý interval je podmnožinou prvého intervalu!")
    else:
        print("Prienikom intervalov je interval(", a, ",", d, ")")
elif c == b and d!=a:
    print("Prienikom je bod", b)
elif d == a and c!=b:
    print("Prienikom je bod", a)
else:
    print("Intervaly nemajú prienik!")
