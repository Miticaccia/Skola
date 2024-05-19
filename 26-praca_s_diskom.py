mena=[]
premenna = open('priezviska.txt', 'r')
riadok = premenna.readline()
pocetMien=0
while riadok != '':
    mena.append(riadok.strip())
    riadok = premenna.readline()
    
print(mena)
premenna.close()
opakovat=True
while opakovat:
    hladaneMeno=input('Zadaj zaciatocne pismeno hladaneho mena:')
    for i in range(len(mena)):
        if (hladaneMeno == mena[i][0] or hladaneMeno.upper() == mena[i][0]  ):
            pocetMien=pocetMien + 1
            print("Meno " + mena[i]+" sa nachadza v zozname")
    if pocetMien==0:
        print("Je nam luto ale meno zacinajuce na "+ hladaneMeno+" sa nenachadza v zozname")
    print('Pocet mien v subore je:',pocetMien)
    opakuj=input('Opakovat hladanie? :')
    pocetMien=0
    if (opakuj!= 'A' and opakuj !='a'):
        opakovat=False
