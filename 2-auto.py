vzdialenost = int(input("Zadajte vzdialenosť, ktorú prejde auto v metroch: "))
rychlost = int(input("Zadajte rýchlosť auta v km/h: "))
benzin = float(input("Zadajte spotrebu v l/100km: "))

rychlost = rychlost / 3.6
cas = vzdialenost/rychlost 

vzdialenost2 = vzdialenost / 1000
spotreba = vzdialenost2 / 100 * benzin
spotreba = spotreba * 1000

print("Auto prejde vzdialenosť ", vzdialenost, " m za ", cas, " s, pričom spotrebuje", spotreba, " ml paliva")
