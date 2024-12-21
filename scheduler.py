import schedule
import time
from fetch_weather_data import save_live_weather_data

cities = ['Warszawa', 'Berlin', 'Paris', 'London', 'New York']

def job():
    print("Fetching live weather data...")
    save_live_weather_data(cities)

schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
