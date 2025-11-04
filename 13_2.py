import mysql.connector
from flask import Flask


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='nätti1235',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def ICAO_sieppari(ICAO):
    sql = f"SELECT name, municipality FROM airport where ident = '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()



    vastaus = {

    "ICAO" : ICAO,
    "Name"  : tulos[0],
    "Municipality" : tulos[1]

    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)