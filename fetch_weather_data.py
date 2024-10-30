import os
import pandas as pd
import requests

# Function to fetch weather data (assume this is defined)
def fetch_weather_data():
    API_KEY = 'f138eea9c9221b1b1ab9ce7078ca9e41'  # Replace with your actual API key
    CITY = 'Warszawa'         # Replace with your desired city
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

    response = requests.get(URL)
    data = response.json()

    # Extract relevant data
    date = pd.to_datetime('now').strftime('%Y-%m-%d')  # Current date
    temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius

    return date, temperature

# Fetch weather data
date, temperature = fetch_weather_data()

# Create DataFrame with the new data
weather_data = pd.DataFrame({'Date': [date], 'Temperature': [temperature]})

# Define the file path
file_path = 'data/weather_data.csv'

# Check if the file already exists
if not os.path.isfile(file_path):
    # If it doesn't exist, write headers and data
    weather_data.to_csv(file_path, mode='w', header=True, index=False)
else:
    # If it exists, append data without headers
    weather_data.to_csv(file_path, mode='a', header=False, index=False)
