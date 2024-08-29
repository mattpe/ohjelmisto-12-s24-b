# Mod 3 t4

year = int(input("Anna vuosiluku: "))

if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
    print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi.")

# bonus: tulosta kaikki karkausvuodet annettuun vuosilukuun asti
iterator = 0
while iterator < year:
    iterator += 4
    if iterator % 400 == 0 or iterator % 100 != 0:
        print(f"{iterator} on karkausvuosi.")
