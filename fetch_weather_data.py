import os
import pandas as pd
import requests
from dotenv import load_dotenv


load_dotenv()

def fetch_weather_data(cities):
    API_KEY = os.getenv('WEATHER_API_KEY')
    if not API_KEY:
        raise ValueError("API key not found. Set the WEATHER_API_KEY environment variable.")

    data_list = []

    for city in cities:
        URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(URL)
        if response.status_code != 200:
            print(f"Failed to fetch weather data for {city}: {response.status_code}")
            continue

        data = response.json()


        date = pd.to_datetime('now').strftime('%Y-%m-%d %H:%M:%S')
        temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']


        data_list.append({
            'City': city,
            'Date': date,
            'Temperature': temperature,
            'Humidity': humidity,
            'WindSpeed': wind_speed,
            'Description': weather_description
        })

    return data_list


def save_live_weather_data(cities):
    live_data = fetch_weather_data(cities)
    live_weather_df = pd.DataFrame(live_data)

    file_path = 'data/live_weather_data.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


    live_weather_df.to_csv(file_path, index=False)


if __name__ == "__main__":
    cities = ['Warszawa', 'Berlin', 'Paris', 'London', 'New York']
    save_live_weather_data(cities)
