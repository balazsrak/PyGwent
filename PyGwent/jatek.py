import jatekos
import grafika
import random
import kartyak
import szabalyok
import ai
import time
       
"""Játékmenet elejétől végéig"""
def jatszma(nev, jatekos_frakcio, ellenfel_frakcio, nehezseg, ket_ai, screen):
    """Inicializálás"""
    grafika.hatter()
    player1 = jatekos.Jatekos(nev, jatekos_frakcio)
    player2 = jatekos.Jatekos(ellenfel_frakcio+"-Ai", ellenfel_frakcio)
    p1_asztal = []
    p2_asztal = []

    jatekos_kor = grafika.ki_kezd(player1.frakcio)
    jatekos_passzolt = False
    ai_passzolt = False
    jatekos_pontszam = 0
    ai_pontszam = 0

    """A játék vezénylése"""
    while player1.nyert_korok < 2 and player2.nyert_korok < 2: #két nyert körig megy a meccs
        jatekos_pontszam = szabalyok.pontszam(p1_asztal)
        ai_pontszam = szabalyok.pontszam(p2_asztal)

        if len(player1.pakli) == 0:
            jatekos_passzolt = True
        if len(player2.pakli) == 0:
            ai_passzolt = True

        grafika.update(player1, p1_asztal, player2, p2_asztal,
                       jatekos_pontszam, ai_pontszam, screen) #minden kör elején frissítjük a játék állását
        time.sleep(1) #várunk 1 másodpercet minden kör előtt
        
        if not jatekos_passzolt and jatekos_kor % 2 == 0: #játékos kör
            while True:
                if not ket_ai:
                        valasz = grafika.bevitel(player1.pakli, ai_passzolt) #turtle inputon bekérjük a választ
                else:
                    valasz = ai.lep(player1, p1_asztal, jatekos_pontszam,
                                    p2_asztal, ai_pontszam, player2.nyert_korok,
                                    ai_passzolt, nehezseg) #két gép esetén ezt a választ is az ai.py kezeli
                    if valasz != -1:
                        valasz += 1 #tömb indexelés
                if valasz == 0 and not ket_ai:
                    szabalyok.info()
                    continue
                if valasz >= -1 and valasz < len(player1.pakli) + 1:
                    break #ha nem információt kért a játékos, haladunk tovább...
                
            if valasz == -1: 
                jatekos_passzolt = True
            else:
                p1_asztal.append(player1.pakli[valasz - 1])
                del player1.pakli[valasz - 1]                
                szabalyok.specialis_effekt(p1_asztal, p2_asztal,
                                           jatekos_frakcio, ellenfel_frakcio)
                szabalyok.buff_kartyak(p1_asztal, p2_asztal, 0)
                
        if jatekos_kor % 2 == 1 and not ai_passzolt: #ellenfél köre, hasonlóképp...
            evalasz = ai.lep(player2, p2_asztal, ai_pontszam,
                   p1_asztal, jatekos_pontszam, player1.nyert_korok,
                   jatekos_passzolt, nehezseg)

            if evalasz == -1:
                ai_passzolt = True
            else:
                p2_asztal.append(player2.pakli[evalasz])
                del player2.pakli[evalasz]                
                szabalyok.specialis_effekt(p1_asztal, p2_asztal,
                                           jatekos_frakcio, ellenfel_frakcio)
                szabalyok.buff_kartyak(p1_asztal, p2_asztal, 1)
                
        if jatekos_passzolt and ai_passzolt: #vége a körnek, megnézzük ki nyerte
            if jatekos_pontszam > ai_pontszam:
                player1.kort_nyert()
            elif jatekos_pontszam < ai_pontszam:
                player2.kort_nyert()
            else:
                player1.kort_nyert()
                player2.kort_nyert()
            jatekos_passzolt = False
            ai_passzolt = False
            
            szabalyok.asztal_torles(p1_asztal)
            szabalyok.asztal_torles(p2_asztal)
            if player1.frakcio == kartyak.Frakcio(2).name:
                kartyak.nr_passziv(player1.pakli)
            if player2.frakcio == kartyak.Frakcio(2).name:
                kartyak.nr_passziv(player2.pakli)
                
        jatekos_kor += 1 #következő körben a másik játékos lép
        
    if player1.nyert_korok > player2.nyert_korok:   #játékos nyert
        return player1.nev
    elif player1.nyert_korok < player2.nyert_korok: #gép nyert
        return player2.nev
    else:                                           #döntetlen
        if (player1.frakcio != kartyak.Frakcio(1).name and player2.frakcio != kartyak.Frakcio(1).name or
            player1.frakcio == kartyak.Frakcio(1).name and player2.frakcio == kartyak.Frakcio(1).name):
            return None
        elif player1.frakcio == kartyak.Frakcio(1).name: #Nilfgaard passzív: megnyeeri a döntetlen játszmát
            return player1.nev+" (Nilfgaard)"
        else:
            return player2.nev+" (Nilfgaard)"

def eredmeny(nev):
    """A játszma fv végeredménye alapján eredményt hirdetünk"""
    if nev is not None:
        uzenet = "{} nyert!".format(nev)
    else:
        uzenet = "Döntetlen!"
    grafika.nyertes(uzenet)

def jatek(nehezseg, ket_ai, screen):
    """Inicializálja a játékot, majd a játszma végeredménye alapján eredményt """
    grafika.uj_ablak()
    grafika.hatter()
    if not ket_ai:
        nev = grafika.jatekos_nev()
    else:
        nev = "Gép"

    frakcio1 = grafika.frakcio_valasztas("A te frakciód")
    frakcio2 = grafika.frakcio_valasztas("Az ellenfeled frakciója")

    eredmeny(jatszma(nev, frakcio1, frakcio2, nehezseg, ket_ai, screen))

