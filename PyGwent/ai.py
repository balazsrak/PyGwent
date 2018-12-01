import random
import szabalyok

def lep(en, asztalom, pontjaim, ellenfel_asztal,
        ellenfel_pont, ellenfel_nyk, passzolt_e, konnyu):
    """Az ellenfél (vagy a gép) lépéseiért felelős"""
    if konnyu: #alapbeállítással csak random kártyákat dobál az ellenfél
        if passzolt_e and pontjaim > ellenfel_pont:
            return -1
        else:
            return random.randint(0, len(en.pakli)-1)
    else: #különböző taktikai lehetőségeket végigvizsgál
        dupla = ellenfel_pont * 2
        if pontjaim >= 30 and pontjaim >= dupla:
            return -1
        dupla = round(ellenfel_pont*1.5, 0)
        if en.nyert_korok == 0 and ellenfel_nyk == 0 and pontjaim > dupla:
            return -1

        if passzolt_e and pontjaim > ellenfel_pont:
            return -1
        
        if en.pakli[0].neve == "Biting Frost" or en.pakli[0].neve == "Skellige Storm":
            ellenfel_cc = 0
            for kartya in ellenfel_asztal:
                if kartya.tipus == "cc" and not kartya.hos:
                    ellenfel_cc += 1
            if ellenfel_cc >= 3:
                return 0
        if en.pakli[0].neve == "Impenetrable Fog" or en.pakli[0].neve == "Skellige Storm":
            ellenfel_rc = 0
            for kartya in ellenfel_asztal:
                if kartya.tipus == "rc" and not kartya.hos:
                    ellenfel_rc += 1
            if ellenfel_rc >= 3:
                return 0
        if en.pakli[0].neve == "Torrential Rain":
            ellenfel_s = 0
            for kartya in ellenfel_asztal:
                if kartya.tipus == "s" and not kartya.hos:
                    ellenfel_s += 1
            if ellenfel_s >= 3:
                return 0
        if en.pakli[0].neve == "Scorch":
            max = szabalyok.legerosebb_keres(ellenfel_asztal)
            enyem_max = szabalyok.legerosebb_keres(en.pakli)
            if max > enyem_max and max >= 10:
                return 0

        cc = 0
        rc = 0
        s = 0
        dandelion = False
        villentretenmerth = False
        cow = False
        odimm = False
        for kartya in en.pakli:
            if kartya.tipus == "cc":
                cc += 1
            elif kartya.tipus == "rc":
                rc += 1
            elif kartya.tipus == "s":
                s += 1
            if kartya.neve == "Dandelion":
                dandelion = True
            if kartya.neve == "Villmerth":
                villentretenmerth = True
            if kartya.neve == "Cow":
                cow = True
            if kartya.neve == "Gaunter O'Dimm":
                odimm = True

        if cc >= 5 and dandelion:
            if ellenfel_nyk == 0:
                for i in range(1, len(en.pakli)):
                    if en.pakli[i].tipus != "cc":
                        return i
            for i in range(1, len(en.pakli)):
                if en.pakli[i].tipus == "cc":
                    return i
                
        if villentretenmerth:
            for kartya in ellenfel_asztal:
                if kartya.tipus == "cc" and not kartya.hos and kartya.erosseg >= 10:
                    for i in range(len(en.pakli)):
                        if en.pakli[i].neve == "Villmerth":
                            return i
        dupla = pontjaim*2
        if ellenfel_pont >= 30 and ellenfel_nyk != 1 and dupla < ellenfel_pont:
            return -1

        if cow:
            for i in range(len(en.pakli)):
                if en.pakli[i].neve == "Cow":
                    return i
        if odimm:
            for i in range(len(en.pakli)):
                if en.pakli[i].neve == "Gaunter O'Dimm":
                    return i

        if len(en.pakli) > 2 and en.nyert_korok == 0:
            return 1
        if len(en.pakli) == 1:
            return 0
        else:
            return random.randint(0, len(en.pakli)-1)

