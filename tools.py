# Tools for the weather outfit agent to process user queries

import os
import requests
from helper import summarize_today
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_geolocation(city: str):
    """
    Fetches the geographical coordinates (latitude and longitude) for a given city using the OpenWeatherMap Geocoding API.
    
    Args:
        city (str): The name of the city to look up.
    
    Returns:
        dict: A dictionary containing the latitude ('lat') and longitude ('lon') of the city if found.
              If the city is not found, returns a dictionary with an 'error' key and a descriptive message.
    
    Note:
        Requires the global variable OPENWEATHER_API_KEY to be set with a valid OpenWeatherMap API key.
    """

    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city,
        "limit": 1,  # just the top result
        "appid": OPENWEATHER_API_KEY,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    if not data:
        return {"error": f"Could not find geolocation for {city}"}

    return {"lat": data[0]["lat"], "lon": data[0]["lon"]}


def get_today_weather(lat: float, lon: float):
    """
    Retrieves and summarizes today's weather for a given latitude and longitude using the OpenWeatherMap API.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.

    Returns:
        dict: A summary of today's weather, as returned by the `summarize_today` function.

    Note:
        Requires the global variable `OPENWEATHER_API_KEY` to be set with a valid OpenWeatherMap API key.
    """

    url = "https://api.openweathermap.org/data/3.0/onecall"

    params = {
        "lat": lat,
        "lon": lon,
        "exclude": "minutely,hourly,alerts,current",
        "units": "metric",
        "appid": OPENWEATHER_API_KEY,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    daily_weather_summary = summarize_today(data["daily"][0])
    return daily_weather_summary

