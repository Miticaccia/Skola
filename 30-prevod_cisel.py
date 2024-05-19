dalsi = True
while dalsi == True:
    dekademicke = int(input("Zadajte číslo v dekademickom zápise: "))
    binarne = ""
    while dekademicke > 0:
        binarne = str(dekademicke % 2) + binarne
        dekademicke = dekademicke // 2
    
    print("Premenené číslo v dvojkovej sústave je: ", binarne)

    odpoved = str(input("Chcete znova tadať číslo? (y/n): "))
    if odpoved == "y":
        dalsi = True
    else: 
        dalsi = False