luku = 0

luku = input("Anna luku: ")
if luku == "":
    print("Ohjelma on päättynyt. Suurinta ja pienintä lukua ei löytynyt.")
else:
    pienin = float(luku)
    suurin = float(luku)
    while True:
        luku = input("Anna luku: ")
        if luku == "":
            break
        else:
            luku = float(luku)
            if luku < pienin:
                pienin = luku
            elif suurin < luku:
                suurin = luku

    print(f"Ohjelma on päättynyt. Suurin luku on {suurin} ja pienin luku on {pienin}.")