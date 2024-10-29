class Työntekijä:

    työntekijöiden_lukumäärä = 0
    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkalainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        # haetaan yliluokan metodin printti
        super().tulosta_tiedot()
        # lisätään oma alikuokan printti
        print(f" Tuntipalkkalisen palkka: {self.tuntipalkka} ")

    def tervehdi(self):
        print('Aliluokka Tuntipalkkalainen tervehtii sinua!!!!')

class Kuukausipalkkalainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kuukausipalkkalaisen palkka: {self.kuukausipalkka} ")

työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
t1 = Tuntipalkkalainen('Ulla', 'Sederlöf', 10)
t1.tervehdi()
print(t1.etunimi, t1.sukunimi, t1.tuntipalkka)
työntekijät.append(t1)
työntekijät.append(Kuukausipalkkalainen('Matti', 'Peltoniemi', 10000))

for t in työntekijät:
    t.tulosta_tiedot()


class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus

class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino

class Polkupyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)
        self.vaihteet = vaihteet


pp = Polkupyörä(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)
