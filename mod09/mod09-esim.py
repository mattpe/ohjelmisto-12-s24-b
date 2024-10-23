koirat = [
    {'koira': 'Lissu', 'vuosi': 2015},
    {'koira': 'Reko', 'vuosi': 2016}
]

# print(koirat)
# eka_koira = koirat[0]
# print(eka_koira['koira'])

#-- Määritellään ensin luokka
# Luokka on "ohje" olion luomiselle

class Koira:
    pass

# 2. Olio on luokan ilmentymä
# Pääohjelmasta voi luoda useita olioita

# luodaan koira-olio
ullan_koira = Koira()
elviiran_koira = Koira()

# annetaan koira-olioille ominaisuuksia
# ominaisuudet ovat oliokohtaisia, kaikki ovat koiria,
# mutta nimi, syntymävuosi, karvan laatu tms. muuttuu

ullan_koira.nimi = 'Lissu'
ullan_koira.syntymävuosi = 2015

elviiran_koira.nimi = 'Reko'
elviiran_koira.syntymävuosi = 2016
elviiran_koira.karva = 'lyhyt'

print(ullan_koira)
print(elviiran_koira)
print(f'Ullan koiran nimi on: {ullan_koira.nimi} ja svuosi on {ullan_koira.syntymävuosi}')

# edellisessä esimerkissä tehtiin luokka ilman ominaisuuksia ja metodeja
# olion ominaisuudet annettiin yksi kerrallaan
# tämä on työlästä ja oikea tapa onkin määritellä ja alustaa ominaisuudet luokan avulla

'''
Luokkien perusrakenne
'''

# luokkien nimissä on CamelCase
class LuokanNimi:

    # __init__ on funktion, erityinen sellainen, kutsutaan konstruktoriksi
    # tätä funktiota kutsutaan aina automaattisesti kun luodaan luokasta olio / instanssi
    # alustajan loppuun EI kirjoiteta return-lausetta
    def __init__(self, parametri1, parametri2):
        self.attribuutti1 = parametri1
        self.attribuutti2 = parametri2

    # metodi
    def metodi(self):
        return
    def metodi2(self):
        return

'''
Laajennetaan yllä olevaa Koira-esimerkkiä niin että se alustaa koirien ominaisuudet
'''

class Koira:
    def __init__(self, nimi, syntymävuosi, väri, koko):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.väri = väri
        self.koko = koko

    def printtaa_tiedot(self):
        print(f'Koira nimi on {self.nimi} ja syntymävuosi on {self.syntymävuosi}')
        return

k1 = Koira('Lissu', 2015, 'harmaa', 'iso')
k2 = Koira('Reko', 2016, 'ruskea', 'pieni')

print(k2.väri)
print(k1.koko)

'''
Laajennetaan yllä olevaa ohjelmaa ja tehdään sinne metodi jossa printataan koirien tiedot
'''

k1.printtaa_tiedot()
k2.printtaa_tiedot()