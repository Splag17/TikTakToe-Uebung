#Spielfeldeingabematrix erstellt
Spielfeld = [
            ["" ,"" ,""],
            ["" ,"" ,""],
            ["" ,"" ,""]]


#Spielzug durchführen (Feld wählen)
def spielzug(Zug):    
    
    if Zug % 2 == 0:
        Eingabe = input("\nSpieler2: Wähle dein Feld (Zeile,Spalte): ")
        Spieler = 2
    else:
        Eingabe = input("\nSpieler1: Wähle dein Feld (Zeile,Spalte): ")
        Spieler = 1

    Zeile, Spalte = map(int, Eingabe.split(","))
#>>>>>>>>>>>>>>>>> Hier noch ausschließen, dass Eingaben unter 1 und über 3 gemacht werden! <<<<<<<<<<<<<<<<<<<<<
    return Zeile - 1, Spalte - 1, Spieler


# Prüfen gewähltes Feld schon belegt ist und Feldwert befuellen
def prüfe_eingabe(Zeile, Spalte, Spieler):

    if Spielfeld[Zeile][Spalte] == 1:
        print('Dieses Feld ist leider schon mit einem "X" belegt.')
    elif Spielfeld[Zeile][Spalte] == 2:
        print('Dieses Feld ist leider schon mit einem "O" belegt.')
    else:
        Spielfeld[Zeile][Spalte] = Spieler

    return Spielfeld


# X oder O nach Eingabe ausgeben
def place_xo(n,i):

    if Spielfeld[n-1][i-1] == 1:
        return("X")
    elif Spielfeld[n-1][i-1] == 2:
        return("O")
    else:
        return(" ")


#Feld mit Nutzereingaben zeichnen
def draw_field():

    print("        |        |        ")
    print(f"   {place_xo(1,1)}    |    {place_xo(1,2)}   |    {place_xo(1,3)}    ")
    print("________|________|________") 
    print("        |        |        ")
    print(f"   {place_xo(2,1)}    |    {place_xo(2,2)}   |    {place_xo(2,3)}    ")
    print("________|________|________") 
    print("        |        |        ")
    print(f"   {place_xo(3,1)}    |    {place_xo(3,2)}   |    {place_xo(3,3)}    ")
    print("        |        |        ")


#Kontrolle der Zeilen und Spalten der Matrix nach 3 in einer Reihe
def check_win():
    x = 1

    while x <= 2:  
        for z in range(3):
 
            if Spielfeld[z] == [x, x, x]:
                    print(f"Spieler{x} hat gewonnen!")  

            elif all(Spielfeld[i][z] == x for i in range(3)):
                    print(f"Spieler{x} hat gewonnen!") 

            #Diagonal fehlt noch!    
        x += 1     
       

#Allgemeiner Spielablauf
draw_field()

for x in range(9):
    Zeile, Spalte, Spieler = spielzug(x)
    prüfe_eingabe(Zeile, Spalte, Spieler)
    draw_field()
    check_win()