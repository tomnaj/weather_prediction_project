import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import  mean_absolute_error, mean_squared_error

def evaluate_model(data, train_ratio=0.8):
    # Split data into train and test sets
    train_size = int(len(data) * train_ratio)
    train_data = data[:train_size]
    test_data = data[train_size:]

    # Train the model
    model = ARIMA(train_data["Temperature"].dropna(), order=(1, 1, 1))
    model_fit = model.fit()

    # Forecast the test period
    forecast_steps = len(test_data)
    forecasted_values = model_fit.forecast(steps=forecast_steps)

    # Get actual values
    actual_values = test_data["Temperature"].values

    # Calculate evaluation metrics
    mae = mean_absolute_error(actual_values, forecasted_values)
    rmse = np.sqrt(mean_squared_error(actual_values, forecasted_values))

    return mae, rmse, forecasted_values, actual_values, test_data.index

def load_historical_data():
    try:
        # Load historical data from CSV
        data = pd.read_csv("data/weather_data.csv", parse_dates=["Date"], index_col="Date")

        # Set frequency to daily
        data = data.asfreq('D')

        return data
    except Exception as e:
        print("Error loading historical data:", e)
        return pd.DataFrame(columns=['Date', 'Temperature'])

def train_model(data):
    model = ARIMA(data["Temperature"].dropna(), order=(1, 1, 1))
    model_fit = model.fit()
    return model_fit

def forecast(model, steps=7):
    return model.forecast(steps=steps)


