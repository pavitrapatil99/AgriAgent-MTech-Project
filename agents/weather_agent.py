
def analyze_weather(rainfall_mm, temperature_c):
    """
    Basic weather analysis using rainfall and temperature.
    These thresholds are illustrative, not crop-specific advice.
    """

    if rainfall_mm < 10 and temperature_c > 30:
        assessment = "Low rainfall and high temperature: check soil moisture"
    elif rainfall_mm >= 10:
        assessment = "Rainfall recorded: assess actual field moisture"
    else:
        assessment = "Continue monitoring local weather conditions"

    return {
        "rainfall_mm": rainfall_mm,
        "temperature_c": temperature_c,
        "assessment": assessment
    }

def analyze_combined_weather(weather_df):
    """
    Analyze historical and forecast weather separately.
    """

    historical = weather_df[
        weather_df["data_type"] == "Historical"
    ]

    forecast = weather_df[
        weather_df["data_type"] == "Forecast"
    ]

    result = {
        "historical_days": len(historical),
        "forecast_days": len(forecast),
        "historical_rainfall_mm": round(
            historical["rainfall"].sum(), 2
        ),
        "forecast_rainfall_mm": round(
            forecast["rainfall"].sum(), 2
        ),
        "historical_avg_temperature_c": round(
            historical["temperature"].mean(), 2
        ),
        "forecast_avg_temperature_c": round(
            forecast["temperature"].mean(), 2
        )
    }

    return result
