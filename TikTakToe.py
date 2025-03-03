#Spielfeldeingabe erstellt
Spielfeld = [
            ["" ,"" ,""],
            ["" ,"" ,""],
            ["" ,"" ,""]]

#Spielfeld visualisieren
# def draw_field():
#     Zeile = 3
#     Spalte = 2

#     for y in range(Zeile):
#         for x in range (Spalte):
#             print("         |         |         ")

#         if y < 2:
#             print("_________|_________|_________") 

#         if y == 1:
#             Spalte = 3 


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
    return Zeile - 1, Spalte - 1, Spieler


def prüfe_eingabe(Zeile, Spalte, Spieler):

    if Spielfeld[Zeile][Spalte] == 1:
        print('Dieses Feld ist leider schon mit einem "X" belegt.')
    elif Spielfeld[Zeile][Spalte] == 2:
        print('Dieses Feld ist leider schon mit einem "O" belegt.')
    else:
        Spielfeld[Zeile][Spalte] = Spieler

    return Spielfeld


def printXO(n,i):
    if Spielfeld[n-1][i-1] == 1:
        return("X")
    elif Spielfeld[n-1][i-1] == 2:
        return("O")
    else:
        return(" ")


def drawField():
    print("        |        |        ")
    print(f"   {printXO(1,1)}    |    {printXO(1,2)}   |    {printXO(1,3)}    ")
    print("________|________|________") 
    print("        |        |        ")
    print(f"   {printXO(2,1)}    |    {printXO(2,2)}   |    {printXO(2,3)}    ")
    print("________|________|________") 
    print("        |        |        ")
    print(f"   {printXO(3,1)}    |    {printXO(3,2)}   |    {printXO(3,3)}    ")
    print("        |        |        ")

#Tests
drawField()
Zug = 6
Zeile, Spalte, Spieler = spielzug()
prüfe_eingabe(Zeile, Spalte, Spieler)
print(Spielfeld)
drawField()