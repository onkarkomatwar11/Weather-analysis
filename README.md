# Weather Data Tracker

This project is a Weather Data Tracking System built using **Streamlit**, **SQLite**, and **Plotly**. The system fetches weather data for a specified city using the **WeatherStack API**, stores it in a lightweight SQLite database, and allows users to analyze and visualize the most recent data.

## Features

- Fetch weather data for a specified city (temperature, humidity, wind speed).
- Store the fetched data in an SQLite database.
- Analyze the most recent weather data and display it.
- Visualize the selected metric using different types of graphs (line, bar, scatter) using **Plotly**.

## How It Works

1. **Fetch Data**: The app allows users to enter a city name, and it fetches weather data using the WeatherStack API.
2. **Store Data**: The fetched data is stored in an SQLite database to ensure data persistence.
3. **Analyze and Visualize**: Users can choose a metric (temperature, humidity, or wind speed) from a dropdown and visualize the data with different graph types (line, bar, scatter).

## Installation and Running the Project

### Prerequisites

- Python 3.9 or higher

### Step-by-Step Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/weather-data-tracker.git
   cd weather-data-tracker

   Usage

Enter the city name in the input field to fetch the weather data.
Click on "Fetch Weather Data" to store the current data.
Use the dropdowns to choose the metric (Temperature, Humidity, Wind Speed) and graph type (Line, Bar, Scatter).
Click on "Analyze Latest Data" to visualize the data.
Project Requirements
Python: Version 3.9 or higher.
Streamlit: For building the web UI.
SQLite: For storing weather data in a lightweight local database.
Plotly: For interactive visualizations.


API Key
To use the WeatherStack API, you need an API key. Replace the value of api_key in the Python code with your actual key.

Credits
Onkar Komatwar: onkarkomatwar11@gmail.com

