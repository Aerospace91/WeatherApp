from api_key import API_KEY
import requests
import json

base_url = "https://api.openweathermap.org/data/3.0/onecall"
geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"

api_key = API_KEY

geo_params = {
    'q': 'Alameda,California',
    'appid': api_key,
    'limit': 1
}

def api_call(url, params, geo=False):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f'Successfully received from: {url}')
    else:
        print(f'Request failed with status code: {response.status_code}')
    if geo == True:
        return data[0]['lat'], data[0]['lon']
    if geo == False:
        return data

lat, lon = api_call(geocoding_url, geo_params, True)

print(f"Latitude is: {lat}")
print(f"Longitude is: {lon}")

weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'units': 'imperial',
    'exclude': 'minutely'
}

weather_response = api_call(base_url, weather_params)

weather_response_dump = json.dumps(weather_response, indent=4)
