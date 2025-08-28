import random

vastaus = random.randint(1,10)

luku = int(input("Arvaa kokonaisluku väliltä 1...10: "))

if luku == vastaus:
    print("Uskomatonta. Arvasit heti oikein!")
else:
    while luku != vastaus:
        if luku < vastaus:
            print("Liian pieni arvaus.")
        elif vastaus < luku:
            print("Liian suuri arvaus.")
        luku = int(input("Arvaa uudelleen: "))
    print("Oikein.")