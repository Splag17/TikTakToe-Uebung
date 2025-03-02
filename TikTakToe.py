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

drawField()

    
