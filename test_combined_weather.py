from utils.weather_agent import get_combined_weather

weather = get_combined_weather()

print("\nCombined Historical and Forecast Weather")
print(weather.to_string(index=False))

print("\nData source summary:")
print(weather["data_type"].value_counts())