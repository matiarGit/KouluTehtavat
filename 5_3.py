luku = int(input("Anna kokonaisluku: "))

x = 0

for i in range(2, luku):
    if luku % i == 0:
        x = 1

if x == 0:
    print("On alkuluku.")
else:
    print("Ei ole alkuluku.")