# Weather_App_with_Tkinter
 This project is a simple desktop application for fetching and displaying weather information for cities using an API and a graphical user interface built with Tkinter.


## Introduction
This project is a desktop application built with `Tkinter` that fetches real-time weather data for a given city. It uses the `geopy` library to find the city’s geographical coordinates and the `OpenWeatherMap` API to retrieve weather conditions. The app also displays the local time based on the city’s timezone using the `TimezoneFinder` and `pytz` libraries.

## Features
- **Location Input**: Users can input the name of any city to retrieve its weather conditions.
- **Real-Time Weather Data**: Fetches real-time data, including temperature, weather conditions, and humidity using OpenWeatherMap.
- **Timezone Adjustment**: Automatically adjusts the displayed time to the city's local timezone.
- **User-Friendly Interface**: Built using `Tkinter` for a simple and interactive user experience.
  
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Weather-App-Tkinter.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Python script:
   ```bash
   python Weather_App.py
   ```
2. Enter the name of a city in the input field, and the app will display the current weather conditions and local time.

## Future Enhancements
- Add more weather details like wind speed and forecast.
- Implement error handling for invalid city names or API errors.
- Enhance the user interface with additional styling and icons.

## API Key
To use the weather API, make sure to replace the placeholder API key with your own from [OpenWeatherMap](https://openweathermap.org/).


