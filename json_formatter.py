import json
import datetime

def convert_timestamp_to_datetime(timestamp):
    #Converting timestamp to datetime object
    datetime_obj = datetime.datetime.fromtimestamp(timestamp)
    return datetime_obj

def toTextualDescription(degree):
    if degree>337.5:
        return 'Northerly'
    if degree>292.5:
        return 'North Westerly'
    if degree>247.5:
        return 'Westerly'
    if degree>202.5:
        return 'South Westerly'
    if degree>157.5:
        return 'Southerly'
    if degree>122.5:
        return 'South Easterly'
    if degree>67.5:
        return 'Easterly'
    if degree>22.5:
        return 'North Easterly'
    return 'Northerly'

json_file_path = "dump.json"

with open(json_file_path) as file:
    data = json.load(file)
    
current_data = data['current']

degree = current_data['wind_deg']

print(f"Latitude: {data['lat']}")
print(f"Longitude: {data['lon']}")
print(f"Timezone: {data['timezone']}")
print(f"Timezone Offset: {data['timezone_offset']}")
print(f"Current Weather:")
print(f" - Current Date and Time: {convert_timestamp_to_datetime(current_data['dt'])}")
print(f" - Sunrise Time: {convert_timestamp_to_datetime(current_data['sunrise'])}")
print(f" - Sunset Time: {convert_timestamp_to_datetime(current_data['sunset'])}")
print(f" - Temperature: {current_data['temp']} fahrenheit")
print(f" - Feel Like Temperature: {current_data['feels_like']} fahrenheit")
print(f" - Pressure: {current_data['pressure']}")
print(f" - Humidity: {current_data['humidity']}")
print(f" - Dew Point: {current_data['dew_point']}")
print(f" - Uvi: {current_data['uvi']}")
print(f" - Wind Speed: {current_data['wind_speed']} mph")
print(f" - Wind Degree: {toTextualDescription(degree)}")
print(f" - Weather Description: {current_data['weather'][0]['description']}")
# print(f" - {current_data[]}")
