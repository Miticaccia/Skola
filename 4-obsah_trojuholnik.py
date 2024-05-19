základna = float(input("Zadajte dĺžku strany(základne): "))
výška = float(input("Zadajte dĺžku výšky na túto stranu: "))
interval1 = float(input("Zadajte počiatočnú hodnotu intervalu: "))
interval2 = float(input("Zadajte konečnú hodnotu intervalu: "))


obsah = výška * základna / 2
print("\nObsah tohto trojuholnika je: ", obsah,"cm\u00b2.")

if obsah > interval1 and obsah < interval2:
    print("Obsah patrí do zadaného intervalu.")
else:
    print("Obsah nepatrí do zadaného intervalu.")