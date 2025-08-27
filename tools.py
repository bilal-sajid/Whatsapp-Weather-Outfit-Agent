import os
import requests
from helper import summarize_today
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_geolocation(city: str):
    """
    Get latitude & longitude for a given city using OpenWeatherMap Geocoding API.
    Returns a dict with just lat/lon.
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
    Get today's weather given latitude and longitude.
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

