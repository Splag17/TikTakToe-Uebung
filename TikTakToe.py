#Spielfeldeingabematrix erstellt
Spielfeld = [
            ["" ,"" ,""],
            ["" ,"" ,""],
            ["" ,"" ,""]]


#Spielzug durchführen (Feld wählen)
def spielzug(Zug):    
    
    if Zug % 2 == 0:
        Eingabe = input("\n\033[93mSpieler1: Wähle dein Feld (Zeile,Spalte): \033[0m")
        Spieler = 1
    else:
        Eingabe = input("\n\033[96mSpieler2: Wähle dein Feld (Zeile,Spalte): \033[0m")
        Spieler = 2

    Zeile, Spalte = map(int, Eingabe.split(","))
    return Zeile - 1, Spalte - 1, Spieler


# Prüfen, ob gewähltes Feld schon belegt ist und Feldwert befuellen
def prüfe_eingabe(Zeile, Spalte, Spieler):
    Blocked = 0
    
    if Spielfeld[Zeile][Spalte] == 1:
        print('\n\033[91mDieses Feld ist leider schon mit einem "X" belegt.\033[0m')
        Blocked = 1
    elif Spielfeld[Zeile][Spalte] == 2:
        print('\n\033[91mDieses Feld ist leider schon mit einem "O" belegt.\033[0m')
        Blocked = 1
    else:
        Spielfeld[Zeile][Spalte] = Spieler

    return Spielfeld, Blocked


# X oder O nach Eingabe ausgeben
def place_xo(n,i):

    if Spielfeld[n-1][i-1] == 1:
        return("\033[93mX\033[0m")
    elif Spielfeld[n-1][i-1] == 2:
        return("\033[96mO\033[0m")
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

    while x <= 2:         
        
        for z in range(3):
 
            if Spielfeld[z] == [x, x, x]:
                print(f"\nSpieler{x} hat gewonnen!")
                return 1  
            elif all(Spielfeld[i][z] == x for i in range(3)):
                print(f"\nSpieler{x} hat gewonnen!") 
                return 1

        if all(Spielfeld[i][i] == x for i in range(3)):
            print(f"\nSpieler{x} hat gewonnen!")
            return 1
        elif all(Spielfeld[i][2-i] == x for i in range(3)):
            print(f"\nSpieler{x} hat gewonnen!") 
            return 1       
        else:
            x += 1         
   
    
       

#Allgemeiner Spielablauf
import os
os.system('cls')
draw_field()

for x in range(9):    
    y = 0                                                                              
    Win = check_win()

    if Win == 1:
        break
    else:
        Zeile, Spalte, Spieler = spielzug(x)

        while y == 0: 

            if 0 <= Zeile < 3  and 0 <= Spalte < 3:
                Spielfeld, Blocked = prüfe_eingabe(Zeile, Spalte, Spieler)

                if Blocked == 0:
                    os.system('cls')                                                
                    draw_field()                                 
                    y += 1
                else:
                    print("\033[91mWähle ein anderes Feld\033[0m")
                    Zeile, Spalte, Spieler = spielzug(x)
                
            else:
                print("\n\033[91mFalsche Eingabe. Erlaubt sind nur Zahlen von 1-3!\033[0m")
                Zeile, Spalte, Spieler = spielzug(x)

if Win == 1:
    print('''\n\033[92m---------------------------------------------
Das Spiel ist vorbei. Herzlichen Glückwunsch!
---------------------------------------------\033[0m\n''')
else:
     print('''\n\033[95m---------------------------------------------
Das Spiel ist vorbei. Keiner hat gewonnen :(
---------------------------------------------\033[0m\n''')

input()