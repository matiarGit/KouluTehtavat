import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def tulostus(self):
        print(f"Rekisteritunnus on {self.rekisteritunnus}.")
        print(f"Huippunopeus on {self.huippunopeus} km/h.")
        print(f"Tämänhetkinen nopeus on {self.nopeus} km/h.")
        print(f"Kuljettu matka on {self.matka} km.")
        print("")

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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,akkukapasiteetti, nopeus, matka=0):
        self.akkukapasiteetti=akkukapasiteetti
        self.nopeus = nopeus
        self.matka = matka
        super().__init__(rekisteritunnus,huippunopeus,nopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko, nopeus, matka=0):
        self.bensatankin_koko = bensatankin_koko
        self.nopeus = nopeus
        self.matka = matka
        super().__init__(rekisteritunnus,huippunopeus,nopeus)


auto1 = Sahkoauto("ABC-15",180,52.5,50)
auto2 = Polttomoottoriauto("ACD-123",165,32.3,50)

for i in range(3):
    Auto.kiihdytä(auto1,random.randint(-10,15))
    Auto.kiihdytä(auto2,random.randint(-10,15))
    Auto.kulje(auto1,1)
    Auto.kulje(auto2,1)

Auto.tulostus(auto1)
Auto.tulostus(auto2)