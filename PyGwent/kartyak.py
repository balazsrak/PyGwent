import random
from enum import Enum

class Frakcio(Enum):
    """Ezekre hivatkozunk a függvényekben és a fájlnevekben"""
    NILFGAARD = 1
    NORTHERN_REALMS = 2
    SCOIATAEL = 3
    MONSTER = 4
    SKELLIGE = 5

class Kartya:
    def __init__(self, neve, tipus, erosseg, hos):
        self.neve = neve
        self.tipus = tipus
        self.erosseg = int(erosseg)
        self.hos = True if hos == "h" else False
        self.eredeti_erosseg = int(erosseg)
            
    def gyengites(self):
        if self.erosseg >= self.eredeti_erosseg:
            self.erosseg = 1
        
    def skellige_effekt(self):
        if self.erosseg >= self.eredeti_erosseg:
            self.erosseg //= 2

    def clear_weather(self):
        self.erosseg = self.eredeti_erosseg
        
    def dandelion(self):
        self.erosseg *= 2

def rendez(lista):
    """Selection sort 8. előadásról: rendezve adjuk a kártyákat a játékosnak"""
    for i in range(1, len(lista)-1):
        minidx = i
        for j in range(i+1, len(lista)):
            if lista[j].erosseg < lista[minidx].erosseg:
                minidx = j
 
        if minidx != i:
            temp = lista[minidx]
            lista[minidx] = lista[i]
            lista[i] = temp

def osztas(kar, seml, spec):
    """Összeállít egy paklit a beolvasott kártyákból a játékosnak"""
    kezbe = random.sample(spec, 1)
    kezbe += random.sample(kar, 8)
    kezbe += random.sample(seml, 7)

    rendez(kezbe)
    return kezbe

def pakliba_beolvas(fajl):
    """Beolvassuk a megfelelő fájlokból a kártyákat, és paklit építünk belőle"""
    lista = []
    with open(fajl) as f:
        for sor in f:
            sor = sor[:-1]
            kartya = sor.split(";")
            if len(kartya) < 3:
                continue
            lista.append(Kartya(kartya[0], kartya[1], kartya[2], kartya[3]))
    return lista

def keveres(frakcio):
    """Kártyák keveréséért felelős (fájlkezelés)"""
    frakcio += ".dat"
    kartyak = []
    semleges_kartyak = []
    specialis_kartyak = []
    try:
        kartyak = pakliba_beolvas(frakcio)
        semleges_kartyak = pakliba_beolvas("neutral.dat")
        specialis_kartyak = pakliba_beolvas("special.dat")
        if frakcio != "SKELLIGE":
            del specialis_kartyak[4]
    except FileNotFoundError:
        print("Hibás vagy hiányzó kártya adatfájl!")

    return osztas(kartyak, semleges_kartyak, specialis_kartyak)

def nr_passziv(pakli):
    """Northern Realms frakció passzív: minde kör végén kap egy ajándék kártyát"""
    lista = []
    try:
        lista = pakliba_beolvas(Frakcio(2).name+".dat")
    except FileNotFoundError:
        print("Hibás vagy hiányzó kártya adatfájl!")

    pakli += (random.sample(lista, 1))
    rendez(pakli)

def uj_adatok():
    """Új kártya feltöltése a kártya adatfájlokba"""
    lista = []
    print("Mi legyen a kártya neve?")
    kartya = input()
    lista.append(kartya)
    while True:
        print("Milyen típusú legyen? (cc, rc vagy s)")
        kartya = input()
        if kartya == "cc" or kartya == "rc" or kartya == "s":
            break
    lista.append(kartya)
    while True:
        try:
            print("Milyen erős legyen? (1-15)")
            kartya = input()
            if int(kartya) >= 1 and int(kartya) <= 15:
                break
        except:
            continue
    lista.append(kartya)
    return lista

def beolvas(fajl):
    """Beolvasunk fájlból"""
    lista = []
    with open(fajl) as f:
        for sor in f:
            lista.append(sor)
    return lista

def hozzaad(frak):
    """Új kártya hozzáadása"""
    lista = []
    if frak == 6:
        neve = "neutral.dat"
        lista = beolvas(neve)
    else:
        neve = Frakcio(frak).name+".dat"
        lista = beolvas(neve)
    lista.append("\n")
    uj_kartya = uj_adatok()
    lista.append(uj_kartya[0]+";"+uj_kartya[1]+";"+uj_kartya[2]+";"+"n\n")
    with open(neve, "w") as f:
        for kartya in lista:
            f.write(kartya)

def torol(frak):
    """Kártya törlése"""
    lista = []
    if frak == 6:
        neve = "neutral.dat"
        lista = pakliba_beolvas(neve)
    else:
        neve = Frakcio(frak).name+".dat"
        lista = pakliba_beolvas(neve)
    for i in range(len(lista)):
        if (not lista[i].hos and lista[i].neve != "Dandelion" and lista[i].neve != "Gaunter O'Dimm" and
            lista[i].neve != "Villmerth" and "Crown:" not in lista[i].neve):
            print(str(i) + ": " + lista[i].neve)
    print("Törlésre szánt kártya sorszáma (0-{}):".format(len(lista)-1))
    while True:
        try:
            torlendo = int(input())
            del lista[torlendo]
            break
        except:
            print("Rossz válasz!")
            continue
    with open(neve, "w") as f:
        for kartya in lista:
            sor = kartya.neve + ";" + kartya.tipus + ";" + str(kartya.erosseg) + ";"
            if kartya.hos:
                sor += "h\n"
            else:
                sor += "n\n"
            f.write(sor)            

def mod():
    """Kártyafájlok módosítása: törlés vagy beszúrás"""
    print("Új kártya beillesztése: 0")
    print("Meglévő kártya törlése: 1")
    modosit = int(input())
    if modosit == 0:
        print("Melyik frakcióhoz szeretnél kártyát hozzáadni?")
        for i in range(0, 5):
            print("{}: {}".format(i + 1, Frakcio(i+1).name))
        print("6: Neutral")
        valasz = int(input())
        if valasz > 0 and valasz < 7:
            hozzaad(valasz)
    elif modosit == 1:
        print("Melyik frakció kártyáját szeretnéd törölni?")
        for i in range(0, 5):
            print("{}: {}".format(i + 1, Frakcio(i+1).name))
        print("6: Neutral")
        valasz = int(input())
        if valasz > 0 and valasz < 7:
            torol(valasz)
