nimet = {""}

while True:
    testi = nimet
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(nimi)

for i in nimet:
    print(i)