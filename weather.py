import requests

city=input("Enter Your City --> ")
Api_Key = "f6e949e13d8a4d77cfd1bd545f9e11df" # Paste Your API ID Here

final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)

result = requests.get(final_URL)
data = result.json()
print(data)

temprature = data['main']['temp']
feels_like = data['main']['feels_like']
cordinatelon = data['coord']['lon']
cordinatelat = data['coord']['lat']

print(f"Temperature: {temprature}")
print(f"Feels Like: {feels_like}")
print(f"Latitude: {cordinatelat}")
print(f"Longitiude: {cordinatelon}")
