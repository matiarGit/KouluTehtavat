#importataan random-moduuli
import random

#Käytetään random-moduulin randint-funktiota.
#Luodaan kolme lukua ohjeiden antamien välien mukaan
luku1 = random.randint(0,9)
luku2 = random.randint(0,9)
luku3 = random.randint(0,9)

#Luodaan neljä numeroa ohjeiden antamien välien mukaan
nro1 = random.randint(1,6)
nro2 = random.randint(1,6)
nro3 = random.randint(1,6)
nro4 = random.randint(1,6)

#Printataan luodut koodit
print(f"Numerolukon 1 koodi on: {luku1}{luku2}{luku3}")
print(f"Numerolukon 2 koodi on: {nro1}{nro2}{nro3}{nro4}")