import random

# MONIKKO ()
##################
print('\nMONIKKO ()\n')

# Monikko (tuple) on "kuin lista jota ei voi muokata"

minun_lista = [1, 2, 3, 4, 5, 6]
print(minun_lista)

minun_monikko = (1, 2, 3, 4, 5, 6)
# minun_monikko = 1, 2, 3, 4, 5, 6
print(minun_monikko)

minun_monikko2 = (1, 2, (3, 4), 5, 'Kuusi')
print(minun_monikko2)

# luetaan ensimmäinen alkio
print(minun_lista[0])
print(minun_monikko[0])

# yritetään nyt muokata eka alkio numeroksi 0 ja lisätä loppuun 7
# listan sisäältöä voi muokata, mutable
minun_lista[0] = 0
minun_lista.append(7)
print(f'Muokattu lista {minun_lista}')

# monikon sisältöä EI voi muokata, immutable
# minun_monikko[0] = 0

# Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on luonteeltaan staattinen:
# tiedetään, että muutoksille ei ole tarvetta ohjelman suorituksen aikana.

'''
# Koodiesimerkki materiaalista
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''

# Monikon läpikäynti kuten listan
# minun_monikko = (1, 2, 3, 4, 5, 6)
minun_monikko3 = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')

for i in minun_monikko3:
    print(i)
    if i == "kolmas":
        print('Kolmas löytyi!!!')
print(minun_monikko3)

# Monikon arvojen purku muuttujiin
hedelmät = ('Lime', 'Sitruuuna', 'Appelsiini')
# (eka, toka, kolmas) = ('Lime', 'Sitruuuna', 'Appelsiini')
(eka, toka, kolmas) = hedelmät
print(eka)

print('\nMonikon voi antaa funktiolle parametrina: \n')

sanalista = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')

print('Terve!')
def tulosta_monikko(sanalista):
    for i in sanalista:
        print(i)

tulosta_monikko(sanalista)
tulosta_monikko(hedelmät)

# perinteinen print ilman paluuarvoa
def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    print(f"Nopista tuli {eka} ja {toka}.")

heitä()

# Monikko funktion paluuarvona
def heitä2():
    (eka, toka) = random.randint(1,6), random.randint(1,6)
    return (eka, toka)

noppa1, noppa2 = heitä2()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

# JOUKKO {}
##################
print('\nJOUKKO {}\n')

# JOUKKO eli set {}

# Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.

# Koska joukon alkioille ei ole määritelty järjestystä, ei alkioihin voi myöskään viitata indeksillä.

# Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen, eli joukossa ei voi olla kahta samansisältöistä alkiota.

# joukko eli set
joukko = {1,2,3,4,5,6,}
# joukko merkataan aaltosulkeilla
print(joukko)

print(f'Numero 6 voi esiintyä listassa useasti:')
minun_lista = [6, 2, 3, 4, 5, 6]
print(minun_lista)

print(f'Numero 6 voi esiintyä monikossa useasti:')
minun_monikko = (6, 2, 3, 4, 5, 6)
print(minun_monikko)

print(f'Numero 6 EI voi esiintyä joukossa useasti:')
minun_joukko = {6, 2, 3, 4, 5, 6}
print(minun_joukko)

# yllä oleva ei sinänsä tuota virhettä, kuten ei add-metodi
minun_joukko.add(6)  # ei onnistu, mutta ei tuota virhettä
minun_joukko.add(7)
print(minun_joukko)
minun_joukko.remove(7)
print(minun_joukko)

# koodiesimerkki, järjestys voi muuttua printatessa
pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

# alkiot iteroidaan läpi for/in rakenteella
for p in pelit:
    print(p)
    # löytyykö Cluedo, jos löytyy printtaa jotain
    if p == "Cluedo":
        print('Cluedo löytyi!!!!')

# if/in haku toimii kuten listoissa
if "Monopoli" in pelit:
    print('Monopoli löytyi!!!')

# Tyhjä joukko luodaan edellä esitetystä poiketen set-funktion avulla.

# tyhjän listan luominen
autolista = []
autolista.append('Audi')
print(autolista)

# tästä tuleekin sanakirja eli dictionary
autojoukko = {}
print(type(autojoukko)) # tämä on <class 'dict'>

# Tyhjä joukko luodaan edellä esitetystä poiketen set-funktion avulla.
autojoukko = set()
autojoukko.add('Audi')
print(type(autojoukko)) # tämä on <class 'set'>
print(autojoukko)

# SANAKIRJA {}
##################
print('\nSANAKIRJA {}\n')

# Sanakirja (dictionary) on Pythonin käytetyimpiä tietorakenteita.
# Sanakirjaan voidaan tallentaa avain-arvopareja.

# Kun sanakirja alustetaan arvot luettelemalla, annetaan kukin avain-arvopari seuraavasti: avain : arvo. Peräkkäiset avain-arvoparit erotellaan toisistaan pilkulla.

oppilaat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 11, 'Daniel': 33, 'Emma': 22}
print(oppilaat)

# mitä ovat tietueet / items
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa?
print(oppilaat.keys())

# mitä ovat arvoja sanakirjassa?
print(oppilaat.values())

# Kun sanakirjaa käydään läpi for/in rakenteella:

# tietueet eli avain-arvoparit
for i in oppilaat.items():
    print(i)

# Kun sanakirja läpikäydään for/in-rakennetta käyttäen,
# saa kierrosmuuttuja arvokseen vuoron perään kunkin sanakirjassa esiintyvän avaimen.

for i in oppilaat:
    print(i)

# oppilaat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 11, 'Daniel': 33, 'Emma': 22}

# yksittäisen arvon haku avaimen avulla
avain = 'Aapeli'
oppilaat['Aapeli']
print(oppilaat[avain]) # etsii avaimella Aapeli sen arvoa joka on 25

# etsi kaikki arvot
for i in oppilaat:
    print(oppilaat[i])
'''
# if / in rakenteella voidaaan myös hakea sanakirjasta tietoa
nimi = input('Anna nimi, niin etsin sen sanakirjasta jos löytyy: ')
if nimi in oppilaat:
    print(f'Löytyi oppilas {nimi} ikä hänellä on {oppilaat[nimi]}')
'''

# Kun olemassa olevaan sanakirjaan lisätään arvo,
# käytetään notaatiota sanakirja[avain] = arvo

# listätään uusi oppilas mikäli ei löydy
# jos avain löytyy, se muokkaa olemassa olevaa, muuten luodaan uusi
oppilaat['Ulla'] = 22
print(oppilaat)





