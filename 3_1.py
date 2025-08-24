kuha = float(input("Anna kuhan pituus: "))
if kuha < 37:
    kuha = 37 - kuha
    print(f"Kuhasi on {kuha} senttimetriä liian lyhyt")
else: print("Kuha on hyvän mittainen :)")