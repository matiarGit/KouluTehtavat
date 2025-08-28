import random

N = 0
n = 0

while N < 1000000:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    N += 1

pii = 4*n/N
print(pii)