import streamlit as st
import requests
import sqlite3
import pandas as pd
import plotly.express as px

# Set up the database
def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            observation_time TEXT
        )
    ''')
    conn.commit()
    return conn

# Function to fetch weather data
def fetch_weather(city):
    api_key = "b69e40835bb2e01a5053fcd164322df9"  # Replace with your API key
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url).json()
    
    if 'current' in response:
        data = {
            'city': city,
            'temperature': response['current']['temperature'],
            'humidity': response['current']['humidity'],
            'wind_speed': response['current']['wind_speed'],
            'observation_time': response['location']['localtime']
        }
        return data
    else:
        return None

# Function to store data in SQLite
def store_weather_data(conn, data):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, temperature, humidity, wind_speed, observation_time)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['city'], data['temperature'], data['humidity'], data['wind_speed'], data['observation_time']))
    conn.commit()

# Function to query the latest weather data from SQLite
def get_latest_weather_data(conn, city):
    cursor = conn.cursor()
    query = '''
        SELECT * FROM weather WHERE city = ? ORDER BY observation_time DESC LIMIT 1
    '''
    cursor.execute(query, (city,))
    data = cursor.fetchone()
    if data:
        return pd.DataFrame([data], columns=['ID', 'City', 'Temperature', 'Humidity', 'Wind Speed', 'Observation Time'])
    else:
        return pd.DataFrame()

# Function to visualize data using Plotly
def plot_weather_data(data, metric, graph_type):
    if not data.empty:
        if metric == "Temperature":
            y_axis = 'Temperature'
        elif metric == "Humidity":
            y_axis = 'Humidity'
        elif metric == "Wind Speed":
            y_axis = 'Wind Speed'
        
        # Plot based on selected graph type
        if graph_type == "Line":
            fig = px.line(data, x='Observation Time', y=y_axis, title=f"{metric} Trend (Line Chart)")
        elif graph_type == "Bar":
            fig = px.bar(data, x='Observation Time', y=y_axis, title=f"{metric} Trend (Bar Chart)")
        elif graph_type == "Scatter":
            fig = px.scatter(data, x='Observation Time', y=y_axis, title=f"{metric} Trend (Scatter Chart)")
        
        st.plotly_chart(fig)

# Streamlit app UI
st.title("Weather Data Tracker")

conn = init_db()

# Input for city
city = st.text_input("Enter City", "New York")

# Fetch and store current weather data
if st.button("Fetch Weather Data"):
    data = fetch_weather(city)
    if data:
        store_weather_data(conn, data)
        st.success(f"Weather data for {city} fetched and stored successfully!")
    else:
        st.error(f"Failed to fetch data for {city}")

# Analyze the most recent weather data
st.write("## Latest Weather Data Analysis")

# Dropdown to select metric
metric = st.selectbox("Select Metric to Analyze", ("Temperature", "Humidity", "Wind Speed"))

# Dropdown to select graph type
graph_type = st.selectbox("Select Graph Type", ("Line", "Bar", "Scatter"))

# Display the latest data analysis
if st.button("Analyze Latest Data"):
    df = get_latest_weather_data(conn, city)
    if not df.empty:
        st.write(df)
        plot_weather_data(df, metric, graph_type)
    else:
        st.error("No data available for the selected city.")
