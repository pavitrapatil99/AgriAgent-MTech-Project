import requests
import pandas as pd


def get_historical_weather(
    latitude,
    longitude,
    start_date,
    end_date
):
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": (
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_sum,"
            "et0_fao_evapotranspiration"
        ),
        "timezone": "Asia/Kolkata"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    if "daily" not in data:
        raise ValueError("Historical weather data is unavailable.")

    df = pd.DataFrame(data["daily"])
    df.rename(columns={
        "time": "date",
        "temperature_2m_max": "max_temperature",
        "temperature_2m_min": "min_temperature",
        "precipitation_sum": "rainfall",
        "et0_fao_evapotranspiration": "reference_et0"
    }, inplace=True)

    return df