#Kysytään leiviskät, naulat ja luodit käyttäjältä

leiviskät = float(input("Anna leiviskät."))

naulat = float(input("Anna naulat."))

luodit = float(input("Anna luodit."))

#Päivitetään muuttujat vastaamaan oikeita painoarvoja annettujen lukujen perusteella

leiviskät = leiviskät * 32 * 20 * 13.3

naulat = naulat * 32 * 13.3

luodit = luodit * 13.3

#Luodaan muuttujat, jotka laskevat kilogrammat, sekä grammat erikseen.

#Kilogramma-muuttujalle saadaan oikea arvo käyttämällä laskutoimitusta //,
#koska sillä saadaan kilojen kokonaisosa.

kilogramma = (leiviskät + naulat + luodit) // 1000

#Gramma-muuttujalla saadaan oikea arvo käyttämällä laskutoimitusta %,
#koska sillä saadaan jakojäännös, eli tässä tapauksessa grammat.

gramma = (leiviskät + naulat + luodit) % 1000

#Printataan annetut tulokset, grammat 2 desimaalin tarkkuudella.

print(f"Massa nykymittojen mukaan:\n{kilogramma} kilogrammaa ja{gramma: .2f} grammaa.")