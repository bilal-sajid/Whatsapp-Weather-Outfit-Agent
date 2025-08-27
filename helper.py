from datetime import datetime

def summarize_today(daily: dict) -> str:
    """
    Turn OpenWeather daily forecast into a clear, outfit-focused English summary.
    """
    # Date
    date = datetime.utcfromtimestamp(daily["dt"]).strftime("%A, %B %d")

    # Temps
    temps = daily["temp"]
    feels = daily["feels_like"]
    t_morn, t_day, t_eve, t_night = round(temps["morn"]), round(temps["day"]), round(temps["eve"]), round(temps["night"])
    f_morn, f_day, f_eve, f_night = round(feels["morn"]), round(feels["day"]), round(feels["eve"]), round(feels["night"])
    
    # Weather / rain
    desc = daily["weather"][0]["description"]
    pop = daily.get("pop", 0.0)  # probability of precipitation (0–1)
    rain_note = ""
    if pop >= 0.6:
        rain_note = f"There is a high chance of rain ({int(pop*100)}%). Bring an umbrella or raincoat."
    elif pop >= 0.3:
        rain_note = f"There is a slight chance of rain ({int(pop*100)}%). A light layer might be useful."

    # Wind
    wind_kmh = round(daily.get("wind_speed", 0.0) * 3.6)
    wind_note = f"Winds will be around {wind_kmh} km/h."

    # UV
    uvi = daily.get("uvi", 0)
    if uvi >= 8:
        uv_note = "UV radiation will be very high — sunscreen and a hat are strongly recommended."
    elif uvi >= 6:
        uv_note = "UV radiation will be high — consider sunscreen if outdoors."
    elif uvi >= 3:
        uv_note = "Moderate UV radiation — sunscreen advisable for longer exposure."
    else:
        uv_note = "Low UV radiation — minimal sun protection needed."

    # Build summary
    return (
        f"Today's Summary ({date}):\n"
        f"- General conditions: {desc}.\n"
        f"- Temperatures: morning {t_morn}°C (feels {f_morn}°C), "
        f"afternoon {t_day}°C (feels {f_day}°C), "
        f"evening {t_eve}°C (feels {f_eve}°C), "
        f"night {t_night}°C (feels {f_night}°C).\n"
        f"- {wind_note}\n"
        f"- {rain_note if rain_note else 'No significant rain expected.'}\n"
        f"- {uv_note}"
    )