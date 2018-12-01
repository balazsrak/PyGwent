import kartyak

class Jatekos:
    def __init__(self, nev, frakcio):
        self.nev = nev
        self.frakcio = frakcio
        self.pakli = kartyak.keveres(self.frakcio)
        self.nyert_korok = 0

    def kort_nyert(self):
        self.nyert_korok += 1

