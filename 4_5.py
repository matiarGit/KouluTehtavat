ktunnus = "python"
salasana = "rules"
ktunnus_arvaus = 0
salasana_arvaus = 0
yritys = 1

while True:
    ktunnus_arvaus = input("Anna käyttäjätunnus: ")
    salasana_arvaus = input("Anna salasana: ")
    if ktunnus_arvaus == "python" and salasana_arvaus == "rules":
        print("Tervetuloa")
        break
    elif yritys == 5:
        print("Pääsy evätty.")
        break
    else:
        print("Yritä uudelleen.")
    yritys += 1