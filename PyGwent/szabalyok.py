import kartyak

BF_aktiv = False

def pontszam (kartyak):
    """Számon tartja, mennyi pontja van a letett kártyáknak"""
    osszeg = 0
    for kartya in kartyak:
        if len(kartya.tipus) <= 2:
            osszeg += kartya.erosseg
    return osszeg

def asztal_torles(asztal):
    """Körök között előkészíti az asztalt"""
    Odimm = False
    Cow = False
    while len(asztal) > 0:
        if asztal[0].neve == "Gaunter O'Dimm":
            Odimm = True
        if asztal[0].neve == "Cow":
            Cow = True
        del asztal[0]
    if Odimm:
        for i in range(2):
            asztal.append(kartyak.Kartya("Darkness", "rc", 4, "n"))
    if Cow:
        asztal.append(kartyak.Kartya("Bovine DF", "cc", 8, "n"))
    BF_aktiv = False

def gyengit(frakcio, asztal, mit):
    """Elvégzi a gyengítő effektet az adott kártyákon"""
    for i in range(len(asztal)):
        if asztal[i].tipus == mit and not asztal[i].hos:
            if frakcio != kartyak.Frakcio(5).name:
                asztal[i].gyengites()
            else:
                asztal[i].skellige_effekt()

def gyengitest_keres(asztal1, asztal2, f1, f2, mit):
    """Kiválogatja, melyik gyengítő effektet kell aktiválni"""
    if "SC/RC" == mit:
        BF_aktiv = True
        gyengit(f1, asztal1, "cc")
        gyengit(f1, asztal1, "rc")
        gyengit(f2, asztal2, "cc")
        gyengit(f2, asztal2, "rc")
    elif "SCC" == mit:
        BF_aktiv = True
        gyengit(f1, asztal1, "cc")
        gyengit(f2, asztal2, "cc")
    elif "SRC" == mit:
        gyengit(f1, asztal1, "rc")
        gyengit(f2, asztal2, "rc")
    elif "SSE" == mit:
        gyengit(f1, asztal1, "s")
        gyengit(f2, asztal2, "s")

def clear_weather(asztal1, asztal2):
    """A gyengítő effektet(ha van) eltávolítja, eredeti kártyaerőket visszaállítja"""
    for i in range(len(asztal1)):
        asztal1[i].clear_weather()
    for i in range(len(asztal2)):
        asztal2[i].clear_weather()
    BF_aktiv = False

def legerosebb_keres(asztal):
    """Maximumkiválasztás: legerősebb nem-hős kártyákat megkeresi"""
    max = 0
    for kartya in asztal:
        if kartya.erosseg > max and not kartya.hos:
            max = kartya.erosseg
    return max

def eleget(asztal, max):
    """Scorch kártya effektje: elégeti a legerősebb nem-hős kártyákat"""
    i = 0
    if len(asztal) > 0:
        while i < len(asztal):
            if asztal[i].erosseg == max and not asztal[i].hos:
                del asztal[i]
                if i != 0:
                    i -= 1
                continue
            i += 1

def scorch(asztal1, asztal2):
    """Maximumkeresés Scorch kártyához"""
    max1 = legerosebb_keres(asztal1)
    max2 = legerosebb_keres(asztal2)
    maximum = max(max1, max2)

    eleget(asztal1, maximum)
    eleget(asztal2, maximum)

def specialis_effekt(asztal1, asztal2, f1, f2):
    """Megkeresi, hogy van-e letett speciális kártya"""
    for kartya in asztal1:
        if len(kartya.tipus) > 2 and kartya.tipus != "SALL":
            gyengitest_keres(asztal1, asztal2, f1, f2, kartya.tipus)
            break
        elif kartya.neve == "Clear Weather":
            for i in range(len(asztal2)):
                if len(asztal2[i].tipus) > 2 and asztal2[i].tipus != "SALL":
                    del asztal2[i]
                    clear_weather(asztal1, asztal2)
                    asztal1.pop()
                    break
        elif kartya.neve == "Scorch":
            scorch(asztal1, asztal2)
            asztal1.pop()
            break
                
    for kartya in asztal2:
        if len(kartya.tipus) > 2 and kartya.tipus != "SALL":
            gyengitest_keres(asztal1, asztal2, f1, f2, kartya.tipus)
            break
        elif kartya.neve == "Clear Weather":
            for i in range(len(asztal1)):
                if len(asztal1[i].tipus) > 2 and asztal1[i].tipus != "SALL":
                    del asztal1[i]
                    clear_weather(asztal1, asztal2)
                    asztal2.pop()
                    break
        elif kartya.neve == "Scorch":
            scorch(asztal1, asztal2)
            asztal2.pop()
            break

def dandelion(asztal):
    """Aktiválja Dandelion erősítését: 2x szorzó minden nem-hős CC kártyára"""
    if asztal[len(asztal)-1].neve == "Dandelion":
        for i in range(len(asztal)):
            if asztal[i].tipus == "cc" and not asztal[i].hos and asztal[i].erosseg <= asztal[i].eredeti_erosseg:
                asztal[i].dandelion()
    else:
        i = len(asztal)-1
        if asztal[i].tipus == "cc" and not asztal[i].hos and asztal[i].erosseg <= asztal[i].eredeti_erosseg:
            asztal[i].dandelion()

def villmerth(asztal):
    """Elégeti az elenfél legerősebb nem-hős cc kártyáit"""
    max = 0
    for kartya in asztal:
        if kartya.tipus == "cc" and not kartya.hos and kartya.erosseg > max:
            max = kartya.erosseg
    i = 0
    if len(asztal) > 0:
        while i < len(asztal):
            if asztal[i].tipus == "cc" and not asztal[i].hos and asztal[i].erosseg == max:
                del asztal[i]
                i -= 1
                continue
            i += 1

def buff_kartyak(asztal1, asztal2, ki):
    """Megkeresi a speciális képességgel rendelkező kártyákat"""
    if len(asztal1) > 0:
        for kartya in asztal1:
            if kartya.neve == "Dandelion" and not BF_aktiv:
                dandelion(asztal1)
        if ki == 0:
            if asztal1[len(asztal1)-1].neve == "Villmerth":
                villmerth(asztal2)
        if "Crone:" in asztal1[len(asztal1)-1].neve:
            asztal1.append(kartyak.Kartya("Fiend", "cc", 6, "n"))
    if len(asztal2) > 0:
        for kartya in asztal2:
            if kartya.neve == "Dandelion" and not BF_aktiv:
                dandelion(asztal2)
        if ki == 1:
            if asztal2[len(asztal2)-1].neve == "Villmerth":
                villmerth(asztal1)
        if "Crone:" in asztal2[len(asztal2)-1].neve:
            asztal2.append(kartyak.Kartya("Fiend", "cc", 6, "n"))

def info():
    """Konzolra megjeleníti a speciális tudnivalókat"""
    with open("info.dat", encoding="utf-8") as f:
        for sor in f:
            print(sor)

