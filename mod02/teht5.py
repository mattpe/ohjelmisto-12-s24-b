# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

leiviskat = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

# ensin selvitetään kuinka paljon meillä on nauloja
naulatTot = leiviskat * 20 + naulat

# sitten selvitellään kuinka paljon meillä on luoteja yhteensä
luoditTot = naulatTot * 32 + luodit

# nyt kun tiedämme määrän niin lasketaan massa ensin grammoina
grammatTot = luoditTot * 13.3
print (grammatTot)

# Lisäksi on olemassa jakojäännösoperaatio (%), pelkän kokonaisosan palauttava jakolasku (//)

kg = int(grammatTot // 1000)
gr = grammatTot % 1000
print(f'Massa nykymittojen mukaan: {kg} kg ja {gr:.2f} grammaa')




