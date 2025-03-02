#Spielfeldeingabe erstellt
Spielfeld = [
            ["" ,"" ,""],
            ["" ,"" ,""],
            ["" ,"" ,""]]

#Spielfeld visualisieren
def draw_field():
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
def spielzug():    
    
    if Zug % 2 == 0:
        Eingabe = input("\nSpieler2: Wähle dein Feld (Zeile,Spalte): ")
        Spieler = 2
    else:
        Eingabe = input("\nSpieler1: Wähle dein Feld (Zeile,Spalte): ")
        Spieler = 1

    Zeile, Spalte = map(int, Eingabe.split(","))
#>>>>>>>>>>>>>>>>> Hier noch ausschließen, dass Eingaben unter 1 und über 3 gemacht werden! <<<<<<<<<<<<<<<<<<<<<
    return Zeile, Spalte, Spieler


def prüfe_eingabe(Zeile, Spalte, Spieler):

    if Spielfeld[Zeile, Spalte] == 1:
        print('Dieses Feld ist leider schon mit einem "X" belegt.')
    elif Spielfeld[Zeile, Spalte] == 2:
        print('Dieses Feld ist leider schon mit einem "O" belegt.')
    else:
        Spielfeld[Zeile,Spalte] = Spieler

    print(Spielfeld)
    return Spielfeld


#Tests
draw_field()
Zug = 5
print(spielzug())
print(type(spielzug()[1]))
