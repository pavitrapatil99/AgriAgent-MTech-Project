
from utils.weather_api import get_hourly_forecast

try:
    data = get_hourly_forecast()

    print("Open-Meteo API connected successfully!")
    print("\nLocation:", data.get("timezone"))
    print("Available hourly readings:", len(data["hourly"]["time"]))

    for i in range(5):
        print(
            data["hourly"]["time"][i],
            "| Temperature:", data["hourly"]["temperature_2m"][i], "°C",
            "| Humidity:", data["hourly"]["relative_humidity_2m"][i], "%",
            "| Precipitation:", data["hourly"]["precipitation"][i], "mm"
        )

except Exception as error:
    print("Weather API test failed:", error)
