import math

# Syötteen lukeminen ja sijoittaminen muuttujaan
name = input("Anna nimesi: ")
# name = "Matti" # merkkijono (string)
# \ on escape-merkki, jolla voi tuottaa esim. tabin tai rivinvaihdon
print("Moi \t " + name) # "Moi " + "Matti" -> "Moi Matti"

# age = "7"
# käyttäjän syöte on aina merkkijono
age = input("Anna ikäsi: ")
print("Ikäsi on " + age)

# Muutetaan merkkijono (str) kokonaisluvuksi (int) ja lisätään 1
age = int(age) + 1 # "7" -> 7 + 1 -> 8
# esitellään uusi muuttuja, johon sijoitetaan numeroarvo merkkjonon tyyppisenä
age_string = str(age) # muutetaan int -> string, esim. 8 -> "8"
print("Ikäsi on vuoden päästä " + age_string)
age = age + 1
# toinen tapa, tehdään tyyppimuunnos vain tarvittavaan kohtaan
print("Ikäsi on kahden vuoden päästä " + str(age))

# käyttäjän pituus metreinä, liukuluku (float)
# height = 1.8
# kysytään pituus käyttäjältä ja muutetaan samantien liukuluvuksi
height = float(input("Anna pituus (m): "))
# kasvatetaan käyttäjään 10 cm
height = height + 0.1
# tulos f-string muodossa, ei tarvita str()-funktiota
print(f"Nimi: {name}, Ikä: {age}, Pituus: {height:.2f} metriä.")

# luetaan piin likiarvon math-paketista (import-lauseet aina tiedoston alkuun)
print(math.pi)