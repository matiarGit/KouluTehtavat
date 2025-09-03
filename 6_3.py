def bensa(gallonit):
    return gallonit * 3.785

i = 1

while i > 0:
    i = float(input("Kuinka monta gallonia? "))
    litra = bensa(i)
    print(f"Se on {litra} litraa.")
