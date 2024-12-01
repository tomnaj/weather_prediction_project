import os
import pandas as pd
import requests
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from a .env file
load_dotenv()

# Function to fetch weather data
def fetch_weather_data():
    API_KEY = os.getenv('WEATHER_API_KEY')  # Get the API key from the environment variables
    if not API_KEY:
        raise ValueError("API key not found. Set the WEATHER_API_KEY environment variable.")
    
    CITY = 'Warszawa'  # Replace with your desired city
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather data: {response.status_code}")
    
    data = response.json()

    # Extract relevant data
    date = pd.to_datetime('now').strftime('%Y-%m-%d')  # Current date
    temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius

    return date, temperature

# Fetch weather data
try:
    date, temperature = fetch_weather_data()
    # Create DataFrame with the new data
    weather_data = pd.DataFrame({'Date': [date], 'Temperature': [temperature]})

    # Define the file path
    file_path = 'data/weather_data.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists

    # Check if the file already exists
    if not os.path.isfile(file_path):
        # If it doesn't exist, write headers and data
        weather_data.to_csv(file_path, mode='w', header=True, index=False)
    else:
        # If it exists, append data without headers
        weather_data.to_csv(file_path, mode='a', header=False, index=False)
except Exception as e:
    print(f"Error: {e}")
