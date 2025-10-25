class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros=alin_kerros
        self.ylin_kerros=ylin_kerros
        self.nykyinen_kerros = alin_kerros
        #self.hissin_nro = hissin_nro

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

class Talo:
    def __init__(self,alin_kerros,ylin_kerros,hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        self.hissi_lista = []
        for i in range(hissien_lkm):
            hissi = Hissi(alin_kerros,ylin_kerros)
            self.hissi_lista.append(hissi)

    def ajahissiä(self, hissi_nro, tavoite_kerros):
        Hissi.siirry_kerrokseen(talo.hissi_lista[hissi_nro],tavoite_kerros)

talo = Talo(-2,10,3)
talo.ajahissiä(0,5)