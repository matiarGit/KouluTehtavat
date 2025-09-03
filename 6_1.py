import random

#Käytetään muuttujaa i seuraamaan nopan arvoja

i = 0

def laskerandom():
    return random.randint(1, 6)

while i != 6:
    i = laskerandom()
    print(i)