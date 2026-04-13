import sys, json, requests

if len(sys.argv) > 3:
    print("Usage: script.py zipcode country_code")
    sys.exit()

url1=f'http://api.openweathermap.org/geo/1.0/zip?zip={sys.argv[1]},{sys.argv[2]}&appid=722077ed6642e30952f11eb8fb5063c0'
response1=requests.get(url1)
longlat=json.loads(response1.text)

url2=f'https://api.openweathermap.org/data/2.5/weather?lat={longlat["lat"]}&lon={longlat["lon"]}&appid=722077ed6642e30952f11eb8fb5063c0'
response2=requests.get(url2)
response2.raise_for_status

weatherdata=json.loads(response2.text)
print(f"{weatherdata['weather'][0]['description']}\nTemperature: {weatherdata['main']['feels_like']- 273}\nHumidity: {weatherdata['main']['humidity']}")