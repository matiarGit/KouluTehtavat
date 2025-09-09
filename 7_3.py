lentoasemat = {"Helsinki-Vantaa" : "EFHK",
               "Heathrow" : "EGLL",
               "Charles De Gaulle" : "LFPG",
               "Frankfurt" : "EDDF",
               "Narita" : "RJAA",}

while True:
    z = input("Mitä haluat tehdä? (hae/tallenna/lopeta): ")
    if z == "lopeta":
        break
    elif z == "hae":
        haku = input("Minkä lentokentän haluat hakea: ")
        if haku in lentoasemat:
            print(f"{haku} lentokentän ICAO koodi on {lentoasemat[haku]}.")
        else:
            print("Syötteessä havaittiin virhe. Hakua ei kyetty suorittamaan loppuun.")
    elif z == "tallenna":
        tallennusLentokentta = input("Anna lentokentän nimi: ")
        tallennusICAO = input("Anna kyseisen lentokentä ICAO-koodi: ")
        lentoasemat[tallennusLentokentta] = tallennusICAO
    else:
        print("Syötteessä tapahtui virhe. Syötä ohjeiden mukaan uudelleen.")
print("Kiitos käynnistä!")