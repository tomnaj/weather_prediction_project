import os
import pandas as pd

# Create your DataFrame
weather_data = pd.DataFrame({'Date': [], 'Temperature': []})

# Check if the file already exists
file_path = 'data/weather_data.csv'
if not os.path.isfile(file_path):
    # If it doesn't exist, write headers
    weather_data.to_csv(file_path, mode='w', header=True, index=False)
else:
    # If it exists, append without headers
    weather_data.to_csv(file_path, mode='a', header=False, index=False)
