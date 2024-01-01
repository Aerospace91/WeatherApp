import tkinter as tk
import json_formatter

window = tk.Tk()
greeting = tk.Label(text="Hello World")


data = json_formatter.load_json()
current_data = data['current']
hourly_data = data['hourly']
daily_data = data['daily']
degree = current_data['wind_deg']

body = tk.Label(text=f"""Latitude: {data['lat']}
Longitude: {data['lon']}
Timezone: {data['timezone']}
Timezone Offset: {data['timezone_offset']}
Current Weather:
 - Current Date and Time: {json_formatter.convert_timestamp_to_datetime(current_data['dt'])}
 - Sunrise Time: {json_formatter.convert_timestamp_to_datetime(current_data['sunrise'])}
 - Sunset Time: {json_formatter.convert_timestamp_to_datetime(current_data['sunset'])}
 - Temperature: {current_data['temp']} fahrenheit
 - Feel Like Temperature: {current_data['feels_like']} fahrenheit
 - Pressure: {current_data['pressure']}
 - Humidity: {current_data['humidity']}%
 - Dew Point: {current_data['dew_point']}
 - Uvi: {current_data['uvi']}
 - Wind Speed: {current_data['wind_speed']} mph
 - Wind Direction: {json_formatter.deg_to_text(degree)}
 - Weather Description: {current_data['weather'][0]['description']}""")

greeting.pack()
body.pack()
window.mainloop()