a = float(input("Zadajte 1. stranu trojuholníka: "))
b = float(input("Zadajte 2. stranu trojuholníka: "))
c = float(input("Zadajte 3. stranu trojuholníka: "))

if a + b > c and a + c > b and c + b > a:
    print("Tieto strany môžu tvoriť trojuholnik!")
    odpoved = str(input("\nChcete otestovať či je trojuholnik pravouhlý? (y/n)"))
    if odpoved == "y" or odpoved == "Y":
        LS = c*c
        PS = a*a + b*b
        if LS == PS:
            print("Tento trojuholnik je pravouhly!")
        else: 
            print("Tento trojuholnik nie je pravouhly!")
else:
    print("Tieto strany nemôžu tvoriť trojuholnik!")