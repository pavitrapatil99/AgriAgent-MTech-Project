import pandas as pd

from utils.historical_weather import get_historical_weather
from utils.weather_api import get_hourly_forecast


def get_combined_weather(
    latitude=12.9716,
    longitude=77.5946,
    start_date="2026-10-01",
    end_date="2026-10-07"
):
    # Get historical weather
    historical = get_historical_weather(
        latitude,
        longitude,
        start_date,
        end_date
    )

    # Get future weather forecast
    forecast_data = get_hourly_forecast()

    forecast = pd.DataFrame(forecast_data["hourly"])

    forecast.rename(columns={
        "time": "date",
        "temperature_2m": "temperature",
        "relative_humidity_2m": "humidity",
        "precipitation": "rainfall"
    }, inplace=True)

    # Convert forecast hourly data into daily data
    forecast["date"] = pd.to_datetime(forecast["date"]).dt.date

    forecast_daily = forecast.groupby("date").agg({
        "temperature": "mean",
        "humidity": "mean",
        "rainfall": "sum"
    }).reset_index()

    historical["date"] = pd.to_datetime(
        historical["date"]
    ).dt.date

    historical["temperature"] = (
        historical["max_temperature"] +
        historical["min_temperature"]
    ) / 2

    historical["humidity"] = None

    historical["data_type"] = "Historical"

    forecast_daily["data_type"] = "Forecast"
    forecast_daily["reference_et0"] = None

    combined = pd.concat(
        [historical, forecast_daily],
        ignore_index=True,
        sort=False
    )

    return combined.sort_values("date").reset_index(drop=True)