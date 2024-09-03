# funktio-esimerkkejä

import random

def do_something():
    print("Doing")
    print("something")
    return "tässä on palautettava arvo, voi olla ihan minkä tyyppinen vaan"

return_value = do_something()
print(return_value)

# funktio, jolla parametreja (argumentteja)
def combine_strings(string1, string2):
    combination = f"{string1}, {string2}"
    #print(combination)
    return combination

print(combine_strings("auto", "ajaa"))

combination = combine_strings("kuski", "jarruttaa")
combination = combine_strings(combination, "nopeasti")
print(combination)

# yksikertainen laskin, jolle voi antaa vain tasan 3 parametria
def calculate(calc_type, number1, number2):
    if calc_type == "sum":
        return number1 + number2
    elif calc_type == "division":
        return number1 / number2
    #return None # oletustoiminnallisuus

print(calculate("sum", 2.4, 3.5))
print(calculate("division", 2.4, 8))

# ohjelma komentorivikäyttöliittymällä
# (valikkosovellus, josta käynnistettävät aliohjelmat toteutettu funktioina)
def noppa_game():
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

def kukkuu_app():
    max_count = int(input("Montaa kertaa kukutaan? "))
    counter = 0
    while counter < max_count:
        counter = counter + 1
        print(f"{counter}. kerran Kukkuu!")
    print(f"Laskurin arvo lopuksi: {counter}")

command = ""
while command != "lopeta":
    command = input("Komento, kiitos> ")
    if command == "lopeta":
        print("Lopetetaan.")
        # break # "heittää ulos" silmukasta, ei paras ohjelmointikäytäntö
    elif command == "kukkuu":
        kukkuu_app()
    elif command == "noppa":
        noppa_game()
    else:
        print("En ymmärrä komentoa. Yritä uudestaan, kiitti.")
print("Ohjelma sammutettu.")