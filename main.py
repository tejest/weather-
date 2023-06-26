import requests
import json


city=input("enter the city name")

url = f"https://api.weatherapi.com/v1/current.json?key=5dedcc68c215433ca78150536231706&q={city}"

r = requests.get(url)
wic = json.loads(r.text)
print(wic["current"]["temp_c"])
