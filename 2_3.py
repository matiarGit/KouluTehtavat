#Kysytään käyttäjältä suorakulmion kanta ja korkeus:
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

#Lasketaan suorakulmion piiri, eli 2*kanta + 2*korkeus
piiri = 2 * kanta + 2 * korkeus

#Lasketaan suorakulmion pinta-ala, eli kanta*korkeus
ala = kanta * korkeus

#Printataan tulokset 2 desimaalin tarkkuudella
print(f"Suorakulmion piiri on {piiri: .2f} ja pinta-ala on {ala: .2f}")