#Spielfeldeingabematrix erstellt
Spielfeld = [
            ["" ,"" ,""],
            ["" ,"" ,""],
            ["" ,"" ,""]]


#Spielzug durchführen (Feld wählen)
def spielzug(Zug):    
    
    if Zug % 2 == 0:
        Eingabe = input("\nSpieler1: Wähle dein Feld (Zeile,Spalte): ")
        Spieler = 1
    else:
        Eingabe = input("\nSpieler2: Wähle dein Feld (Zeile,Spalte): ")
        Spieler = 2

    Zeile, Spalte = map(int, Eingabe.split(","))
    return Zeile - 1, Spalte - 1, Spieler


# Prüfen gewähltes Feld schon belegt ist und Feldwert befuellen
def prüfe_eingabe(Zeile, Spalte, Spieler):
    Blocked = 0
    
    if Spielfeld[Zeile][Spalte] == 1:
        print('\nDieses Feld ist leider schon mit einem "X" belegt.')
        Blocked = 1
    elif Spielfeld[Zeile][Spalte] == 2:
        print('\nDieses Feld ist leider schon mit einem "O" belegt.')
        Blocked = 1
    else:
        Spielfeld[Zeile][Spalte] = Spieler

    return Spielfeld, Blocked


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

    print("\n        |        |        ")
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
    win = 1

    while x <= 2:         
        
        for z in range(3):
 
            if Spielfeld[z] == [x, x, x]:
                print(f"\nSpieler{x} hat gewonnen!")  
            elif all(Spielfeld[i][z] == x for i in range(3)):
                print(f"\nSpieler{x} hat gewonnen!") 

        if all(Spielfeld[i][i] == x for i in range(3)):
            print(f"\nSpieler{x} hat gewonnen!")
        elif all(Spielfeld[i][2-i] == x for i in range(3)):
            print(f"\nSpieler{x} hat gewonnen!")        
        else:
            win = 0

        x += 1            
    return win
    
       

#Allgemeiner Spielablauf
draw_field()

for x in range(9):
    Zeile, Spalte, Spieler = spielzug(x)
    y = 0    

    while y == 0:    
        if 0 <= Zeile < 3  and 0 <= Spalte < 3:
            Spielfeld, Blocked = prüfe_eingabe(Zeile, Spalte, Spieler)

            if Blocked == 0:
                draw_field()
                check_win()
                y += 1
            else:
                print("Wähle ein anderes Feld")
                Zeile, Spalte, Spieler = spielzug(x)
        
        else:
            print("\nFalsche Eingabe. Erlaubt sind nur Zahlen von 1-3!")
            Zeile, Spalte, Spieler = spielzug(x)