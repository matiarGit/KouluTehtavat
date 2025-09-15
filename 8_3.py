import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='nätti1235',
         autocommit=True
         )

def gps_sieppari(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident = '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return tulos


ICAO1 = input("Anna ensimmäinen ICAO-koodi: ")
ICAO2 = input("Anna toinen ICAO koodi: ")

tulos1 = gps_sieppari(ICAO1)
tulos2 = gps_sieppari(ICAO2)
etaisyys = (distance.distance(tulos1, tulos2).km)

print(f"Etäisyys näiden välillä on {etaisyys} km.")