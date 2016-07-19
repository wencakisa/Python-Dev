import sys
import requests
from datetime import datetime, timezone
from decimal import Decimal

API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=965acdac1ae64cf06761bb563ad34d96'
KELVIN_TO_CELSIUS_SUBTRACT = 273.15


def main():
    city = str(input('Enter a city: '))

    print('. . . Getting weather information . . .')

    resp = requests.get(API_URL.format(city))
    city_info_dict = resp.json()

    if city_info_dict.get('cod') == '404':
        print('Unknown city: {}'.format(city))
        return 1

    timestamp = city_info_dict.get('dt')
    main_info = city_info_dict.get('main')

    temp = Decimal(main_info.get('temp') - KELVIN_TO_CELSIUS_SUBTRACT)
    pressure = main_info.get('pressure')
    humidity = main_info.get('humidity')

    wind_info = city_info_dict.get('wind')

    wind_speed = wind_info.get('speed')

    print('''
Info from {}
Temperature: {:.2f}°C
Pressure: {}p
Humidity: {}%
Wind speed: {}m/s
'''.format(
        datetime.fromtimestamp(timestamp=timestamp, tz=timezone.utc).strftime('%d-%m-%Y %H:%M'),
        temp,
        pressure,
        humidity,
        wind_speed
    ))

    return 0

if __name__ == '__main__':
    sys.exit(main())
