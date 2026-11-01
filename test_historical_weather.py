from utils.historical_weather import get_historical_weather

weather = get_historical_weather(
    latitude=12.9716,
    longitude=77.5946,
    start_date="2026-10-01",
    end_date="2026-10-07"
)

print("\nHistorical Weather Data")
print(weather.to_string(index=False))

print("\nTotal rainfall:")
print(weather["rainfall"].sum(), "mm")