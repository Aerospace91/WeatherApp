import json
import datetime

def convert_timestamp_to_datetime(timestamp):
    #Converting timestamp to datetime object
    datetime_obj = datetime.datetime.fromtimestamp(timestamp)
    return datetime_obj

def deg_to_text(degree):
    # Converting Degree Angle to Wind Direction
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

def load_json(json_file_path="dump.json"):
    with open(json_file_path) as file:
        data = json.load(file)
    return data

def print_report():    
    data = load_json()

    current_data = data['current']
    hourly_data = data['hourly']
    daily_data = data['daily']
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
    print(f" - Humidity: {current_data['humidity']}%")
    print(f" - Dew Point: {current_data['dew_point']}")
    print(f" - Uvi: {current_data['uvi']}")
    print(f" - Wind Speed: {current_data['wind_speed']} mph")
    print(f" - Wind Direction: {deg_to_text(degree)}")
    print(f" - Weather Description: {current_data['weather'][0]['description']}")
    # print(f" - {current_data[]}")

    print(f"Hourly Weather:")
    for hourly in hourly_data:
        print(f"Time: {convert_timestamp_to_datetime(hourly['dt'])}")
        print(f" - Temperature: {hourly['temp']} fahrenheit")
        print(f" - Feels like: {hourly['feels_like']} fahrenheit")
        print(f" - Humidity: {hourly['humidity']}%")
        print(f" - Wind Speed: {hourly['wind_speed']} mph")
        print(f" - Wind Direction: {deg_to_text(hourly['wind_deg'])}")
        print(f" - Weather Description: {hourly['weather'][0]['description']}")
        print()
        
    print("Daily Weather:")
    for daily in daily_data:
        print(f"Time: {convert_timestamp_to_datetime(daily['dt'])}")
        print(f" - Daily Summary: {daily['summary']}")
        print(f" - Temperature:")
        print(f" - - Day: {daily['temp']['day']}")
        print(f" - - Min Temp: {daily['temp']['min']}")
        print(f" - - Max Temp: {daily['temp']['max']}")
        print(f" - - Evening Temp: {daily['temp']['eve']}")
        print(f" - Feels like:")
        print(f" - - Day: {daily['feels_like']['day']}")
        print(f" - - Night: {daily['feels_like']['night']}")
        print(f" - - Evening: {daily['feels_like']['eve']}")
        print(f" - Humidity: {daily['humidity']}%")
        print(f" - Wind Speed: {daily['wind_speed']} mph")
        print(f" - Wind Direction: {deg_to_text(daily['wind_deg'])}")
        print(f" - Weather Description: {daily['weather'][0]['description']}")
        print()