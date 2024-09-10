"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
- Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
- Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

def is_prime_number(num):
    # jätetään nolla ja negatiiviset luvut kokonaan testaamatta
    if num < 1:
        return False
    for i in range(2, num):
        #print(i)
        if num % i == 0:
            # jos jaollinen jollain i:n arvolla, palautetaan false
            # ja funktion suoritus loppuu siihen
            return False
    # jos funktion suoritus on jatkunut tänne asti, niin palautetaan True
    return True

# pääohjelma lukee syötteen ja tulostaa vastauksen
user_input = int(input("Anna testattava kokonaisluku (>0): "))
if is_prime_number(user_input):
    print(f"Luku {user_input} on alkuluku.")
else:
    print(f"Luku {user_input} ei ole alkuluku.")

# testataan ensin funktion toimintaa erilaisilla arvoilla
#print(is_prime_number(4))
#print(is_prime_number(280))
#print(is_prime_number(0))

import random
total = 0
results = [] # extra
dice_count = int(input("Montas noppaa laitetaan? "))
for i in range(dice_count):
    result = random.randint(1, 6)
    total = total + result
    results.append(result)
print(f"Noppien silmälukujen summa on {results}, nopat: {results}")

# mod6t1
def roll_die():
    return random.randint(1, 6)

result = 0
while result !=6:
    result = roll_die()
    print(result)
