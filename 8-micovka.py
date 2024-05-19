suma = int(input("Zadajte sumu na rozklad: "))

hodnoty = [500, 200, 100, 50, 20, 10, 5, 2, 1]
for i in hodnoty:
    if i == 500:
        a = suma // i
        zvysok = suma % i 
        print("Pocet", i, "euroviek je ", a)
    else:
        suma = zvysok
        a = suma // i
        zvysok = suma % i 
        print("Pocet", i, "euroviek je ", a)
