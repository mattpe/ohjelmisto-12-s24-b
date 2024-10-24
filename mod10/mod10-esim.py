class Autotalli:
    def __init__(self):
        self.autot = []
    def auto_sisaan(self, auto):
        self.autot.append(auto)
    def auto_ulos(self):
        return
    def tulosta_inventaario(self):
        print("Autot tallissa:")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()

class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self):
        print(f"Olen {self.nimi}, {self.ika}, ja ajan autoa {self.auto.rek_nro}:")
        self.auto.kiihdyta(40)
        print(self.auto.nopeus)
        self.auto.kiihdyta(140)
        print(self.auto.nopeus)
        self.auto.kiihdyta(-250)
        self.auto.tulosta_ominaisuudet()

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.huippunopeus = huippunopeus
        self.kuljettaja = "Räikkönen"

    def tulosta_ominaisuudet(self):
        print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
        print(f"Tämänhetkinen nopeus: {self.nopeus}")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        # rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0

# luodaan oliot ja sijoitetaan viittauksen niihin muuttujiin
a1 = Auto("ABC-123", 142)
a2 = Auto("ZYX-789", 250)
kuski = Kuljettaja("Räikkönen", 44, a1)
kuski.aja()
# vaihdetaan kuljettajan autoa ja ajetaan uudestaan
kuski.auto = a2
kuski.aja()

# luodaan Autotalli-tyyppinen olio ja sijoitetaan autot sinne
talli = Autotalli()
talli.auto_sisaan(a1)
talli.tulosta_inventaario()
talli.auto_sisaan(a2)
talli.tulosta_inventaario()

#a2.kiihdyta(5)
#print(a2.nopeus)
# mahdollinen mutta huono ohjelmointitapa
#a2.nopeus = a2.nopeus + 300
""""
# käytetään sensijaan olion toimintoja nopeuden muuttamiseen
a2.kiihdyta(300)
a1.kiihdyta(-54)
a1.tulosta_ominaisuudet()
a2.tulosta_ominaisuudet()
a2.kiihdyta(-156)
a2.tulosta_ominaisuudet()
"""
# mod 9 harj 1 esimerkkiratkaisu
#print(f"{a1.rek_nro}, huippunopeus: {a1.huippunopeus}")
#print(f"{a2.rek_nro}, huippunopeus: {a2.huippunopeus}")

"""
## Samaan olioon voi viitata useasta muuttuja
a1 = a2
a1.tulosta_rekkari()
a1.rek_nro = "0"
a2.tulosta_rekkari()
"""


