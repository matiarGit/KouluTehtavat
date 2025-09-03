import random

lista = []

#Tehdään 5-10 pituinen lista numeroita väliltä 1-100

x = random.randint(5,10)

for i in range(x):
    z = random.randint(1, 100)
    lista.append(z)
print(f"Generoitu lista on: {lista}")
print("")

#Määritetään funktio

def numerot(luvut):
    summa = 0
    for i in range(x):
        summa = summa + lista[i]
    print(f"Listan numeroiden summa on: {summa}")

numerot(lista)