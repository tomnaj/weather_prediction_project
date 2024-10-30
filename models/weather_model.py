import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def load_data():
    # Load data from CSV
    try:
        data = pd.read_csv("data/weather_data.csv", parse_dates=["Date"], index_col="Date")

        # Convert the index to datetime
        data.index = pd.to_datetime(data.index)

        # Set frequency to daily
        data = data.asfreq('D')

        return data
    except ValueError as e:
        print("Error loading data:", e)
        return pd.DataFrame(columns=['Date', 'Temperature'])  # Return an empty DataFrame if loading fails

def train_model(data):
    model = ARIMA(data["Temperature"], order=(1,1,1))
    model_fit = model.fit()
    return model_fit

def forecast(model, steps = 7):
    return model.forecast(steps=steps)


