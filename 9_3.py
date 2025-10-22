class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def tulostus(self):
        print(f"Rekisteritunnus on {self.rekisteritunnus}.")
        print(f"Huippunopeus on {self.huippunopeus} km/h.")
        print(f"Tämänhetkinen nopeus on {self.nopeus} km/h.")
        print(f"Kuljettu matka on {self.matka} km.")

    def kiihdytä(self, uusi_nopeus):
        self.nopeus = self.nopeus + uusi_nopeus
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        return self.nopeus

    def kulje(self, aika):
        self.matka = self.matka + self.nopeus * aika

        return self.matka



auto = Auto("ABC-123",142,60,2000)
print(auto.kulje(1.5))
auto.tulostus()
