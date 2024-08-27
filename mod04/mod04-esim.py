import random

# kikkailua loogisilla operaattoreilla
print(not True)
print(True and True)
print(True and False)
print(True or True)
print(True and (False or True))
result = (False or False) and (False or True)
print(f"Vertailun tulos: {result}")
print(1 < 2 or (1 == 1 and result))

# While-silmukat (loopit)
# ikuinen silmukka, ei hyvä!
"""
while True:
    print("Moro")
    print("Matti!")
"""

max_count = int(input("Montaa kertaa kukutaan? "))
counter = 0
while counter < max_count:
    counter = counter + 1 # lyhyt versio: counter += 1
    print(f"{counter}. kerran Kukkuu!")
print(f"Laskurin arvo lopuksi: {counter}")

# tulostetaan 2:n potenssit
x = 2
while x < 1000:
    print(x)
    x *= 2 # sama kuin x = x * 2

# noppasimulaattori (import random)
# mikä on kahden yhtäaikaisen kutosen todennäköisyys?
rounds = 1000
round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        #print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}")
    #print(f"Noppaa heitettiin {roll_counter} kertaa.")
    total_rolls = total_rolls + roll_counter
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla.")

# ohjelma komentorivikäyttöliittymällä
# (valikkosovellus, johon sisällytetty ylläolevat esimerkit)
command = ""
while command != "lopeta":
    command = input("Komento, kiitos> ")
    if command == "lopeta":
        print("Lopetetaan.")
        # break # "heittää ulos" silmukasta, ei paras ohjelmointikäytäntö
    elif command == "kukkuu":
        max_count = int(input("Montaa kertaa kukutaan? "))
        counter = 0
        while counter < max_count:
            counter = counter + 1
            print(f"{counter}. kerran Kukkuu!")
        print(f"Laskurin arvo lopuksi: {counter}")
    elif command == "noppa":
        rounds = 1000
        round_counter = 0
        total_rolls = 0
        while round_counter < rounds:
            round_counter += 1
            die1 = die2 = roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
            total_rolls = total_rolls + roll_counter
        print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla.")
    else:
        print("En ymmärrä komentoa. Yritä uudestaan, kiitti.")
print("Ohjelma sammutettu.")
