---

# Weather Prediction Project

This project uses historical weather data to predict future temperatures. It employs a machine learning model to make forecasts and displays the results using a Streamlit-based web application.

## Features

- Forecast future temperatures for a chosen horizon (up to 14 days).
- Display both historical and forecasted temperatures on an interactive graph.
- Simple user interface built with Streamlit for easy interaction.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/weather_prediction_project.git
   cd weather_prediction_project
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run main.py
   ```

2. **Interact with the application**:
   - Select the forecast horizon (in days) using the slider.
   - View the forecasted temperatures displayed alongside historical data.

## Project Structure

- `main.py`: The main file to run the Streamlit application.
- `models/weather_model.py`: Contains functions for loading data, training the model, and forecasting.
- `requirements.txt`: Lists required packages for the project.

## Example Output

The application will display a graph with the historical temperatures in blue and forecasted temperatures in red, allowing for a clear visualization of temperature trends.

## Contributing

Feel free to open issues or submit pull requests if you would like to contribute.

## License

This project is licensed under the MIT License.

---

