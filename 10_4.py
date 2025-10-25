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

    def listatekijä(self, lkm):
        autolista = []
        for i in range(lkm):
            auto = Auto(f"ABC-{i+1}", random.randint(100,200))
            autolista.append(auto)
        return autolista

class Kilpailu:
    def __init__(self,kilpailun_nimi,kilpailun_pituus,auto_lista):
        self.kilpailun_nimi=kilpailun_nimi
        self.kilpailun_pituus=kilpailun_pituus
        self.auto_lista=auto_lista

    def tunti_kuluu(self):
        for i in range(len(kilpailu.auto_lista)):
            Auto.kiihdytä(autolista[i], random.randint(-10, 15))
            Auto.kulje(autolista[i], 1)

    def tulosta_tilanne(self):
        for i in range(len(kilpailu.auto_lista)):
            Auto.tulostus(kilpailu.auto_lista[i])
    def kilpailu_ohi(self):
        for i in range(len(kilpailu.auto_lista)):
            if kilpailu.auto_lista[i].matka > kilpailu.kilpailun_pituus:
                print("--------------Kilpailu on ohi----------------")
                return True



autolista = Auto.listatekijä(Auto,10)

kilpailu=Kilpailu("Suuri romuralli",8000,autolista)

kierros=0

jatkuuko_kilpailu = "kyllä"
while jatkuuko_kilpailu != "ei":
    kierros +=1
    kilpailu.tunti_kuluu()
    if kilpailu.kilpailu_ohi() == True:
        jatkuuko_kilpailu = "ei"
    if kierros == 10:
        print("--------------10 kierrosta on kulunut----------------")
        kilpailu.tulosta_tilanne()


kilpailu.tulosta_tilanne()