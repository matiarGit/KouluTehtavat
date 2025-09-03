import random

#Käytetään muuttujaa i seuraamaan nopan arvoja

i = 0

sivu = int(input("Kuinka monta sivua nopassa? "))

def laskerandom(tahko):
    return random.randint(1, tahko)

while i != sivu:
    i = laskerandom(sivu)
    print(i)