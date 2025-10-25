class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros=alin_kerros
        self.ylin_kerros=ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"Olet nyt kerroksessa {self.nykyinen_kerros}")
    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Olet nyt kerroksessa {self.nykyinen_kerros}")
    def siirry_kerrokseen(self, tavoite_kerros):
        while self.nykyinen_kerros != tavoite_kerros:
            if self.nykyinen_kerros < tavoite_kerros:
                Hissi.kerros_ylös(self)
            elif self.nykyinen_kerros > tavoite_kerros:
                Hissi.kerros_alas(self)

hissi=Hissi(-2,10)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(-2)