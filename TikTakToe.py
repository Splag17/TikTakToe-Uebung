#Spielfeldeingabe erstellt
Spielfeld = [
            ["" ,"" ,""],
            ["" ,"" ,""],
            ["" ,"" ,""]]

#Spielfeld visualisieren
def drawField():
    Zeile = 3
    Spalte = 2

    for y in range(Zeile):
        for x in range (Spalte):
            print("         |         |         ")

        if y < 2:
            print("_________|_________|_________") 

        if y == 1:
            Spalte = 3 


#Spielzug durchführen (Feld wählen)
def Spielzug():
    
    
    if Zug % 2 == 0:
        Eingabe = input("\nSpieler2: Wähle dein Feld (Zeile,Spalte): ")
        
    else:
        Eingabe = input("\nSpieler1: Wähle dein Feld (Zeile,Spalte): ")

    Zeile, Spalte = Eingabe.split(",")

    return Zeile, Spalte


drawField()
Zug = 5
print(Spielzug())