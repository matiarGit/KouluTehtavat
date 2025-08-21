#Kysytään käyttäjältä ympyrän säde
sade = float(input("Kerro ympyrän säde: "))

#Importataan math-moduuli, jotta voidaan käyttää piin arvoa
import math

#Lasketaan ympyrän pinta-ala säteen avulla. Annetaan tulos 2 desimaalin tarkkuudella.
ala = math.pi * sade ** 2
print(f"Ympyrän pinta-ala on: {ala: .2f}")