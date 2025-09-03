import random

lista = []

parillinenlista = []

#Tehdään 5-10 pituinen lista numeroita väliltä 1-100

x = random.randint(5,10)

for i in range(x):
    z = random.randint(1, 100)
    lista.append(z)
print(f"Generoitu lista on: {lista}")
print("")

#Määritetään funktio

def numerot(luvut):
    for a in range(x):
        if lista[a] % 2 == 0:
            g = lista[a]
            parillinenlista.append(g)
    return parillinenlista

numerot(lista)
print(f"Parittomista luvuista karsittu lista on: {parillinenlista}")