class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self,nimi,kirjailija,sivumaara):
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirjan nimi on {self.nimi}, kirjalija {self.kirjailija} ja sivumaara {self.sivumaara}.")

class Lehti(Julkaisu):
    def __init__(self,nimi,paatoimittaja):
        self.paatoimittaja=paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.nimi} ja päätoimittaja {self.paatoimittaja}.")


kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()