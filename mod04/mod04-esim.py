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
"""
max_count = int(input("Montaa kertaa kukutaan? "))
counter = 0
while counter < max_count:
    counter = counter + 1
    print(f"{counter}. kerran Kukkuu!")
print(f"Laskurin arvo lopuksi: {counter}")
"""

# ohjelma komentorivikäyttöliittymällä
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
    else:
        print("En ymmärrä komentoa. Yritä uudestaan, kiitti.")

print("Ohjelma sammutettu.")
