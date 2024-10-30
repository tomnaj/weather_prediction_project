import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

from models.weather_model import load_data, train_model, forecast

# Load data and train model
data = load_data()
model = train_model(data)

# Streamlit app title and description
st.title("Weather Prediction App")
st.write("This app uses historical weather data to predict future temperatures.")

# Slider for forecast horizon
forecast_days = st.slider("Select forecast horizon (days)", 1, 14, 7)

# Generate forecasted temperatures
forecasted_temps = forecast(model, forecast_days)
forecast_dates = [data.index[-1] + timedelta(days=i) for i in range(1, forecast_days + 1)]

# Create DataFrame for forecasted temperatures
forecast_df = pd.DataFrame({"Date": forecast_dates, "Forecasted Temperature": forecasted_temps})
st.subheader("Forecasted Temperatures")
st.write(forecast_df)

# Set up plot
fig, ax = plt.subplots()

# Ensure 'Temperature' column exists in data and the index is in datetime format
if "Temperature" in data.columns:
    # Convert index to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(data.index):
        data.index = pd.to_datetime(data.index)

    # Plot historical temperatures with their corresponding dates
    data["Temperature"].plot(ax=ax, label="Historical Temperatures", color="blue")

# Ensure that 'Date' is a datetime type for the forecast DataFrame
forecast_df['Date'] = pd.to_datetime(forecast_df['Date'])

# Set 'Date' as the index for plotting
forecast_df.set_index("Date", inplace=True)

# Plot the forecasted temperatures
forecast_df["Forecasted Temperature"].plot(ax=ax, label="Forecasted Temperatures", color="red")

plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Forecast")
plt.legend()
st.pyplot(fig)
