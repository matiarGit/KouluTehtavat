import math

# Laaditaan funktio laskemaan yksikköhintaa:

def pizzalaskuri(halkaisija, hinta):
    sade = halkaisija / 2
    ala = math.pi * sade ** 2
    alametreina = ala / 10000
    yksikkohinta = hinta / alametreina
    print(f"Yksikköhinta tälle pizzalle on {yksikkohinta} eur/m^2")
    return yksikkohinta

#Ensimmäinen pizza:
halkaisija1 = float(input("Anna pizzan halkaisija senttimetreissä: "))
hinta1 = float(input("Anna pizzan hinta euroissa: "))

yksikkohinta1 = pizzalaskuri(halkaisija1, hinta1)

#Toinen pizza:
halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreissä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroissa: "))

yksikkohinta2 = pizzalaskuri(halkaisija2, hinta2)

#Verrataan:
if yksikkohinta1 < yksikkohinta2:
    print(f"Ensimmäisen pizzan yksikköhinta on parempi kuin toisen, sillä {yksikkohinta1}eur/m^2 < {yksikkohinta2}eur/m^2.")
elif yksikkohinta2 < yksikkohinta1:
    print(f"Toisen pizzan yksikköhinta on parempi kuin ensimmäisen, sillä {yksikkohinta2}eur/m^2 < {yksikkohinta1}eur/m^2.")
elif yksikkohinta1 == yksikkohinta2:
    print(f"Molempien pizzojen yksikköhinnat ovat yhtä hyvät, sillä {yksikkohinta2}eur/m^2 = {yksikkohinta1}eur/m^2.")