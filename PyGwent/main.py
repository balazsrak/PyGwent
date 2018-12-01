import jatek
import grafika
import kartyak

def main():

    konnyu = True
    ket_ai = False
    small_screen = False
    grafika.uj_ablak()

    menu = 0
    while True:
        print("Új játék: 0")
        print("Nehézség: 1")
        print("Képernyő beállítások: 2")
        print("Gép a gép ellen: 3")
        print("Kártyalista modifikáció: 4")
        print("Kilépés: 5")
        try:
            menu = int(input())
            if menu == 5:
                break
            elif menu == 1:
                print("Könnyű mód: 0")
                print("Nehéz mód: 1")
                mod = int(input())
                konnyu = True if mod == 0 else False
            elif menu == 2:
                print("Kisebb képernyőre: 0")
                print("Nagyobb képernyőre: 1")
                meret = int(input())
                if meret == 0:
                    small_screen = True
                else:
                    small_screen = False
            elif menu == 3:
                print("Te játszol a gép ellen: 0")
                print("Gép játszik gép ellen: 1")
                mod = int(input())
                ket_ai = True if mod == 1 else False
            elif menu == 4:
                kartyak.mod()
            elif menu == 0:
                jatek.jatek(konnyu, ket_ai, small_screen)
        except:
            continue
main()

