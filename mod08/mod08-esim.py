import mysql.connector

# connect()-funktion palauttaa tietokantayhteyden, joka sijoitetaan muuttujaan
connection = mysql.connector.connect(
                host='127.0.0.1', # localhost
                port=3306,
                database='flight_game3',
                user='username',
                password='password',
                autocommit=True,
                collation='utf8mb4_general_ci'
                )
#print(connection)

# luodaan osoitin ja sijoitetaan muuttujaan
cursor = connection.cursor()
# ajetaan SQL-kielinen kysely osoittimen avulla
sql = "SELECT continent, name, iso_country FROM country"
cursor.execute(sql)
# fetchone hakee rivi kerrallaan, palauttaa monikon
#result = cursor.fetchone()
#print(result)

# fetchmany() palauttaa halutan määrän rivejä (monikko) kerrallaan listana
result = cursor.fetchmany(3)
print(result)
print(f"Tulosrivejä käyty läpi (kursorin sijainti): {cursor.rowcount}")

# fetchall() palautta kaikki (loput) rivit listana
rows = cursor.fetchall()
print(rows)

# tuloslista käsitellään toistorakenteella
for row in rows:
    print(f"{row[1]}, Maakoodi: {row[2]}, maanosa: {row[0]}")
if cursor.rowcount > 0:
    print(f"Tulosrivejä yhteensä: {cursor.rowcount}")
else:
    print("Ei tuloksia.")

