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

auto = Auto("ABC-123",142)
auto.tulostus()