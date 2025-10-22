import random
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

    def listatekijä(self, lkm):
        autolista = []
        for i in range(lkm):
            auto = Auto(f"ABC-{i+1}", random.randint(100,200))
            autolista.append(auto)
        return autolista


autolista = Auto.listatekijä(Auto,10)

jatkuuko_kisa = "kyllä"

while jatkuuko_kisa != "ei":
    for i in range(10):
        Auto.kiihdytä(autolista[i], random.randint(-10,15))
        Auto.kulje(autolista[i], 1)

    for i in range(10):
        if autolista[i].matka > 10000:
            jatkuuko_kisa = "ei"


for i in range(10):
    Auto.tulostus(autolista[i])
    print("")