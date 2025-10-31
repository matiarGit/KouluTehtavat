import requests

kaupunki = input("Minkä kaupungin säätiedot haluat? (kirjoita kaupungin nimi englanniksi): ")

api_key = "ed76947c9b8e5da7f4c784d635ca3fb9"

kaupunki_teksti = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"

kaupunki_request = requests.get(kaupunki_teksti).json()

lon = kaupunki_request["coord"]["lon"]

lat = kaupunki_request["coord"]["lat"]

#tekstiin lisättiin units=metric, milloin lämpötila tulee Celsius-asteina
main_teksti = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"

main_request = requests.get(main_teksti).json()

print(main_request)
print(f"Kaupungissa {kaupunki} on {main_request['main']['temp']} Celsius-astetta lämmintä.")