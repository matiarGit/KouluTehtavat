luokka = input("Mikä on hyttiluokkasi? (LUX, A, B, C)")

if luokka == "LUX":
    print("Hyttisi sisältää parvekkeen ja sijaitsee yläkannella")
elif luokka == "A":
    print("Hyttisi sisältää ikkunan ja sijaitsee autokannen yläpuolella")
elif luokka == "B":
    print("Hyttisi ei sisällä ikkunaa ja sijaitsee autokannen yläpuolella")
elif luokka == "C":
    print("Hytti on ikkunaton ja autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka.")