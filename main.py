import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from models.weather_model import load_historical_data, train_model, forecast


historical_data = load_historical_data()
if historical_data.empty:
    st.error("No historical weather data available. Please run the data collection script first.")
else:
    model = train_model(historical_data)

   
    st.title("Weather Prediction App")
    st.write("This app uses historical weather data to predict future temperatures.")

  
    forecast_days = st.slider("Select forecast horizon (days)", 1, 14, 7)

 
    forecasted_temps = forecast(model, forecast_days)
    forecast_dates = [historical_data.index[-1] + timedelta(days=i) for i in range(1, forecast_days + 1)]

 
    forecast_df = pd.DataFrame({"Date": forecast_dates, "Forecasted Temperature": forecasted_temps})
    st.subheader("Forecasted Temperatures")
    st.write(forecast_df)

    fig, ax = plt.subplots()


    historical_data["Temperature"].plot(ax=ax, label="Historical Temperatures", color="blue")

    # Plot the forecasted temperatures
    forecast_df.set_index("Date", inplace=True)
    forecast_df["Forecasted Temperature"].plot(ax=ax, label="Forecasted Temperatures", color="red")

    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.title("Temperature Forecast")
    plt.legend()
    st.pyplot(fig)


    try:
        live_data = pd.read_csv("data/live_weather_data.csv")
        st.subheader("Live Weather Data")
        st.write(live_data)
    except FileNotFoundError:
        st.warning("Live weather data not available. Please run the data collection script.")


st.subheader("Model Evaluation")
if not historical_data.empty:
    from models.weather_model import evaluate_model

    mae, rmse, forecasted_values, actual_values, test_dates = evaluate_model(historical_data)

    st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
    st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.2f}")


    test_df = pd.DataFrame({
        "Date": test_dates,
        "Actual Temperature": actual_values,
        "Forecasted Temperature": forecasted_values
    }).set_index("Date")

    st.line_chart(test_df)
