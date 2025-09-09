kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
z = int(input("Anna halutun kuukauden numero: "))

kuukausi = kuukaudet[z - 1]
vuodenaika = vuodenajat[(z-1) // 3]

print(f"{kuukausi} on osa vuodenaikaa {vuodenaika}")
