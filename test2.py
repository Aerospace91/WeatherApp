from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic
import json_formatter

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Weather.ui', self)
        self.show()

app = QApplication([])
window = Ui()
window.setObjectName("Weather App")
window.tabWidget.setTabText(0, "Current Weather")
window.tabWidget.setTabText(1, "Daily Weather")

data = json_formatter.load_json()
current_data = data['current']
hourly_data = data['hourly']
daily_data = data['daily']
degree = current_data['wind_deg']

window.label.setText(f"""Latitude: {data['lat']}
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

daily_list = []
for daily in daily_data:
    daily_list.append(f"""Time: {json_formatter.convert_timestamp_to_datetime(daily['dt'])}
     - Daily Summary: {daily['summary']}
     - Temperature:
     - - Day: {daily['temp']['day']}
     - - Min Temp: {daily['temp']['min']}
     - - Max Temp: {daily['temp']['max']}
     - - Evening Temp: {daily['temp']['eve']}
     - Feels like:
     - - Day: {daily['feels_like']['day']}
     - - Night: {daily['feels_like']['night']}
     - - Evening: {daily['feels_like']['eve']}
     - Humidity: {daily['humidity']}%
     - Wind Speed: {daily['wind_speed']} mph
     - Wind Direction: {json_formatter.deg_to_text(daily['wind_deg'])}
     - Weather Description: {daily['weather'][0]['description']}""")
    
window.label_2.setText(daily_list[0])


app.exec()