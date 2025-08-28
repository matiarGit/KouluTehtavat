luvut = []

luku = input("Anna luku: ")

while luku != "":
    luku = float(luku)
    luvut.append(luku)
    luku = input("Anna luku: ")

luvut.sort(reverse=True)
print(f"5 suurinta lukua ovat: {luvut[0:5]}")