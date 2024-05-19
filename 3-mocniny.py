while True:
    základ = float(input("Zadajte kladný základ mocniny: "))
    if základ < 0:
        print("Základ je záporný!")

    exponent = int(input("Zadajte exponent mocniny: "))
    print (exponent,". mocnina z čísla ", základ, " je číslo", základ**exponent )
