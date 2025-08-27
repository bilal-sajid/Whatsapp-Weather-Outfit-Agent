from datetime import datetime

def summarize_today(daily: dict) -> str:
    """
    Turn OpenWeather daily forecast into a clear English summary, broken down into
    Morning, Afternoon, Evening, Night. No outfit suggestions, just weather data.
    """
    # Convert timestamp to readable date
    date = datetime.utcfromtimestamp(daily["dt"]).strftime("%A, %B %d, %Y")

    # Extract temps and feels_like
    temps = daily["temp"]
    feels = daily["feels_like"]

    t_morn, t_day, t_eve, t_night = temps["morn"], temps["day"], temps["eve"], temps["night"]
    f_morn, f_day, f_eve, f_night = feels["morn"], feels["day"], feels["eve"], feels["night"]

    # General info
    desc = daily["weather"][0]["description"]
    wind_kmh = round(daily.get("wind_speed", 0.0) * 3.6)
    gusts = daily.get("wind_gust", None)
    pop = daily.get("pop", 0.0)
    uvi = daily.get("uvi", None)

    # Build sections
    summary = f"Weather Summary for {date}\n"
    summary += f"General conditions: {desc}\n"
    summary += f"Chance of rain: {int(pop*100)}%\n"
    if uvi is not None:
        summary += f"UV Index: {uvi}\n"
    summary += f"Wind: {wind_kmh} km/h"
    if gusts:
        summary += f", gusts up to {round(gusts*3.6)} km/h"
    summary += "\n\n"

    summary += "Morning:\n"
    summary += f"- Temperature: {t_morn:.1f}°C (feels like {f_morn:.1f}°C)\n\n"

    summary += "Afternoon:\n"
    summary += f"- Temperature: {t_day:.1f}°C (feels like {f_day:.1f}°C)\n\n"

    summary += "Evening:\n"
    summary += f"- Temperature: {t_eve:.1f}°C (feels like {f_eve:.1f}°C)\n\n"

    summary += "Night:\n"
    summary += f"- Temperature: {t_night:.1f}°C (feels like {f_night:.1f}°C)\n"

    return summary