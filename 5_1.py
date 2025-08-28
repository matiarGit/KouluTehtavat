import random

arpa = int(input("Montako noppaa?: "))
summa = 0

for i in range(arpa):
    noppa = random.randint(1,6)
    summa += noppa

print(f"Noppien summa on {summa}")