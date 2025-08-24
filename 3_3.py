sukupuoli = input("Kerro sukupuolesi (mies/nainen)")
hemo = float(input("Mikä on hemoglobiiniarvosi?"))
if sukupuoli == "mies":
    if hemo >= 117:
        if hemo <= 175:
            print("Hemoglobiiniarvosi on normaali")
        else:
            print("Hemoglobiiniarvosi on korkea")
    else:
        print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli == "nainen":
    if hemo >= 134:
        if hemo <= 195:
            print("Hemoglobiiniiarvosi on normaali")
        else:
            print("Hemoglobiiniarvosi on korkea")
    else:
        print("Hemoglobiiniarvosi on alhainen")
else:
    print("Jotain meni vastauksessasi pieleeen.")