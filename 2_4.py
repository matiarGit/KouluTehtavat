#Kysytään kolmea kokonaislukua
luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
luku3 = int(input("Anna luku 3: "))

#Lasketaan tulo
tulo = luku1 * luku2 * luku3

#Lasketaan summa
summa = luku1 + luku2 + luku3

#Lasketaan keskiarvo, eli tässä tapauksessa summa/3
keskiarvo = summa / 3

#Printataan arvot käyttäjällä, keskiarvo kahden desimaalin tarkkuudella
print(f"Lukujesi summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo: .2f}.")