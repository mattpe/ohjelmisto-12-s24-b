name1 = "Ville"
name2 = "Liisa"
name3 = "Ulla"
age1 = 3
age2 = 5
age3 = 22
print(f'Hei {name1} ja ikäsi on {age1} vuotta')
print(f'Hei {name2} ja ikäsi on {age2} vuotta')
print(f'Hei {name3} ja ikäsi on {age3} vuotta')
print('-------------')
names = ['Ville', 'Liisa', 'Ulla', 'Anna', 'Matti']
ages = [age1, age2, age3, 45, 67]
print(names)
print(ages)

#names2 = [name1, name2, name3]
#print(names2)

# listan pituus voidaan tarkistaa len() funktiolla
length = len(names)
print(f'Listan pituus on: {length}')

# ages = [age1, age2, age3, 45, 67]

# alkioon viitataan indeksinumerolla
print(f'Hei {names[2]} ikäsi on {ages[2]}')

# Viittaus listan ulkopuolelle tuottaa virheen
#print(names[8]) # tuottaa virheen
print('-------------')

# listan läpikäynti while. silmukan avulla
iterator = 0
# while 0 < 5:
# while 1 < 5:
# while 2 < 5:
# while 3 < 5:
# while 4 < 5:

while iterator < len(names):
    print(f'Hei {names[iterator]} ikäsi on {ages[iterator]}')
    #iterator = iterator + 1
    iterator += 1

# tapoja viitata listan alkioihin
lista = ['Ville', 'Liisa', 'Ulla', 'Anna', 'Matti', 'Ahmed', 'Neo', 'Viivi']
print(lista[2:5]) # 2, 3, 4 (ei viimeistä alkiota), 3 alkiota, indeksistä 2 alkaen
print(lista[2:]) # kaikki loputkin alkiot indeksillä 2 alkaen
print(lista[-1]) # listan viimeinen alkio
print(lista[2:6:2]) # indeksistä 2 indeksiin 6, joka toinen

# listaan voi yhdistää ja siellä voi olla erilaisia tietorakenteita
yhdistetty_lista = [23, 45, 66, 67, 67, ['Ulla', 'Matti', 'Ilkka']]
print(yhdistetty_lista)
print(yhdistetty_lista[5][1])

"""
nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)
"""

print('\n-------------')
print('LISTAOPERAATIOT')

# lista = ['Ville', 'Liisa', 'Ulla', 'Anna', 'Matti', 'Ahmed', 'Neo', 'Viivi']

lista.append('Uusi nimi') # uusi alkio listan loppuun
print(lista)

if "Ulla" in lista:
    print('Ulla löytyi listasta! Ja nyt poistetaan samalla!')
    lista.remove('Ulla') # poistetaan alkio, mikäli se löytyy, muuten virhe
    print(lista)

# pistetään nimi ulla takaisin ensimmäiseksi listan alkioksi
lista.insert(0, 'Ulla')
print(lista)

# monentenako lisätty nimi nyt oikein on?
print(lista.index('Matti'))

lisaa_nimia = ['Ines', 'Aku', 'Tupu', 'Hupu']
lista.extend(lisaa_nimia) # lisää nimet listan perään
# uusi_lista = lista + lisaa_nimia
print(lista)

lista[2] = 'Lisa' # muokataan olemassa olevaa alkiota
print(lista)

lista.sort()
print(lista)

numero_lista = [10000, 2, 4, 45, 5, 600, 7, 8, 9, 10]
numero_lista.sort()
print(numero_lista)

print('\n-------------')
print('Listan läpikäynti for-toistorakenteen avulla\n')

for kirjain in 'abcde':
    print(kirjain)

for alkio in [1, 2, 3, 4, 5]:
    print(alkio)

for nimi in lista:
    print(nimi)

"""
for numero in range(5, 50, 2):
    print(numero)

print('--------')

for i in range(999, 0, -3):
    print(i)
"""
# käytetään edellä olevia iteroimaan nimilistaa läpi
# for silmukka iteraattorilla

print(lista)
for i in range(5): # 0, 1, 2, 3, 4
    print(i)
    print(f'Terve: {lista[i]}')

for nimi in lista:
    print(nimi)

print('---------')
print('Listan pituus rangena:')

listan_pituus = len(lista)
print(f'Lista on {listan_pituus} alkiota pitkä')

# for i in range(len(lista)):
for i in range(listan_pituus): # listan pituus maksimina 0-12
    print(f'Terve: {lista[i]}')















