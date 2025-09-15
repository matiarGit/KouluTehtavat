import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='nätti1235',
         autocommit=True
         )

def ICAO_sieppari(ICAO):
    sql = f"SELECT name, iso_region FROM airport where ident = '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"ICAO-koodille {ICAO} lentoasema on {rivi[0]} ja kunta on {rivi[1]} ")

ICAO = input("Anna ICAO-koodi: ")
ICAO_sieppari(ICAO)