
import requests


def get_hourly_forecast():
    """Fetch the hourly weather forecast for Bengaluru using Open-Meteo."""

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 12.9716,
        "longitude": 77.5946,
        "hourly": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation"
        ),
        "timezone": "Asia/Kolkata",
        "forecast_days": 7,
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    return response.json()
