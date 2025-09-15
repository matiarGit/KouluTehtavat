import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='nätti1235',
         autocommit=True
         )

def tyyppi_sieppari(tyyppi):
    sql = f"SELECT type FROM airport where iso_country = '{tyyppi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    pieni = medium = iso = suljettu = kopteri = 0

    if kursori.rowcount > 0:
        for rivi in tulos:
            if rivi[0] == "small_airport":
                pieni += 1
            elif rivi[0] == "medium_airport":
                medium += 1
            elif rivi[0] == "large_airport":
                iso += 1
            elif rivi[0] == "closed":
                suljettu += 1
            elif rivi[0] == "heliport":
                kopteri += 1

    print(f"Helikopterikenttiä on {kopteri}, pieniä kenttiä {pieni}, keskikokoisia {medium}, isoja {iso} ja suljettuja {suljettu}.")

tyyppi = input("Anna maakoodi: ")
tyyppi_sieppari(tyyppi)