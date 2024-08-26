
# Alustus ehtolauseille

rahat = float(input("Anna rahamääräsi: "))

if rahat >= 5:
    print('Voit ostaa latten, sinulla on tarpeeksi rahaa')

print('Jatketaan pääohjelmaa')


# Sama kuin:
rahat = float(input("Anna rahamääräsi: "))

ehto = (rahat >= 5)
print(ehto)

if ehto:
    #tämä osa on lohko ja suoritetaan jos ehto on totta
    print('Voit ostaa latten, sinulla on tarpeeksi rahaa')
print('Jatketaan pääohjelmaa')

# Python Consolessa tutkimme Boolean tyyppiä, kommennot

A = True
A = true #virhe

B = False
C = 'True' #string

type(3 > 2) #True

# Kokeiltiin läpi kaikkea erilaisia vertailuoperaattoreita, fokus yhtä suuri kuin ==

3 = 3 # virhe
3 == 3 #True
'moi' == 'moi' #True
'moi' == 'Moi' #False
3 == '3' #False, Strict equality pythonissa toisin kuin JS



suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari == räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")


# Luo ohjelma joka pyytää käyttäjän numeron ja tulostaa onko luku pos, neg vai nolla

luku = int(input('Anna luku: '))
if luku > 0 :
    print('Numero on pos')

if luku < 0:
    print('Numero on neg')

if luku == 0:
    print('Numero on 0')


# kaksi toisensa poissulkevaa vaihtoehtoa

rahat = float(input("Anna rahamäärä: "))
if rahat >= 5:
    print('Voit ostaa latten.')
else:
    print('Sinulla valitettavasti ole tarpeeksi rahaa latteen')


# monta vaihtoehtoa

user_input = input('Valitse a, b tai c:  ')
if user_input == 'a':
    print('Tehdään jotain, käyttäjä valitsi kirjaimen a')
elif user_input == 'b':
    print('Tehdään jotain muuta kivaa, käyttäjä valitsi b')
elif user_input == 'c':
    # lohkossa on usein paljonkin koodia ja kaikki sisennetty suoritetaan
    print('Käyttäjä valitsi C')
    print('Moikka saat C luokan hytin')
    a = 4 + 4
    print(f'Saat rahaa buffaan {a}euroa bonuksena')
else:
    print('Käyttäjä ei syöttänyt a, b tai c. Ei tehdä siis mitäään')

print('Ohjelma loppuu, hei hei')

# Loogiset operaattorit

ika = 5
nimi = "Matti"

# lauseke a and b on tosi täsmälleen silloin, kun sekä lauseke a että lauseke b ovat tosia.
# True True
print(ika < 10 and nimi == "Matti" ) #true

# True False
print(ika < 10 and nimi == "Ulla" ) #false

# lauseke a or b on tosi täsmälleen silloin, kun vähintään jompikumpi lausekkeista a ja b on tosi.
print(ika < 10 or nimi == "Ulla") #true



