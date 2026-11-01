
import streamlit as st
from agents.knowledge_agent import get_agricultural_guidance
from utils.weather_api import get_hourly_forecast
from utils.weather_agent import get_combined_weather
from utils.crop_config import CROP_PROFILES, REGION_CONFIG
from agents.satellite_agent import analyze_satellite
from agents.weather_agent import analyze_weather
from agents.supervisor_agent import generate_assessment

st.set_page_config(
    page_title="AgriAgent",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AgriAgent")
st.subheader(
    "Agricultural Decision Support Using Satellite and Weather Intelligence"
)

st.write(
    "Enter sample satellite and weather readings to analyze crop conditions."
)

st.header("Crop Information")

st.header("Regional Information")

st.write(
    f"District: {REGION_CONFIG['district']}, "
    f"State: {REGION_CONFIG['state']}"
)

zone_names = list(
    REGION_CONFIG["agro_climatic_zones"].keys()
)

selected_zone = st.selectbox(
    "Select Agro-Climatic Zone",
    zone_names
)

available_areas = REGION_CONFIG[
    "agro_climatic_zones"
][selected_zone]

selected_area = st.selectbox(
    "Select Taluk / Area",
    available_areas
)
crop_name = st.selectbox(
    "Select Crop",
    list(CROP_PROFILES.keys())
)

growth_stages = CROP_PROFILES[crop_name]["stages"]

growth_stage = st.selectbox(
    "Select Current Growth Stage",
    growth_stages
)

sowing_date = st.date_input(
    "Crop Sowing Date"
)

st.info(
    "This prototype uses sample inputs. It does not yet retrieve live satellite "
    "or weather data."
)


farmer_question = st.text_input(
    "Ask your agricultural question:",
    placeholder="Example: Is my crop experiencing water stress?"
)


st.header("1. Satellite Information")

ndvi = st.slider(
    "Vegetation indicator (NDVI)",
    min_value=-1.0,
    max_value=1.0,
    value=0.45,
    step=0.05
)

st.header("2. Weather Information")

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    max_value=500.0,
    value=5.0,
    step=1.0
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=-10.0,
    max_value=60.0,
    value=32.0,
    step=1.0
)

st.header("Historical and Future Weather Analysis")

if st.button("Fetch Historical and Forecast Weather"):
    try:
        combined_weather = get_combined_weather()

        st.success("Historical and forecast weather retrieved successfully!")

        st.dataframe(
            combined_weather,
            use_container_width=True
        )

        st.subheader("Weather Data Summary")

        st.write(
            combined_weather["data_type"].value_counts()
        )

    except Exception as error:
        st.error(f"Could not retrieve combined weather: {error}")


st.header("Live Weather Forecast — Bengaluru")

if st.button("Fetch Hourly Forecast"):
    try:
        forecast_data = get_hourly_forecast()
        hourly = forecast_data["hourly"]

        forecast_df = {
            "Time": hourly["time"],
            "Temperature (°C)": hourly["temperature_2m"],
            "Humidity (%)": hourly["relative_humidity_2m"],
            "Precipitation (mm)": hourly["precipitation"],
        }

        import pandas as pd

        st.success("Hourly forecast fetched successfully!")
        st.dataframe(
            pd.DataFrame(forecast_df).head(24),
            use_container_width=True
        )

    except Exception as error:
        st.error(f"Could not fetch weather forecast: {error}")


if st.button("Analyze Crop Conditions"):
    satellite_result = analyze_satellite(ndvi)
    weather_result = analyze_weather(rainfall, temperature)

    st.header("3. Analysis Results")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛰️ Satellite Agent")
        st.metric("NDVI", satellite_result["ndvi"])
        st.write(satellite_result["condition"])

    with col2:
        st.subheader("🌦️ Weather Agent")
        st.write(
            f"Rainfall: {weather_result['rainfall_mm']} mm"
        )
        st.write(
            f"Temperature: {weather_result['temperature_c']} °C"
        )
        st.write(weather_result["assessment"])

    st.warning(
        "These are preliminary indicators, not a confirmed diagnosis of crop "
        "water stress. Check soil moisture and crop-specific conditions."
    )

    supervisor_result = generate_assessment(
        satellite_result,
        weather_result
    )

    st.header("4. Supervisor Agent: Combined Assessment")
    st.write(supervisor_result["assessment"])

    st.subheader("Recommended Next Steps")
    st.write(supervisor_result["recommendation"])

    knowledge_result = get_agricultural_guidance(
        farmer_question,
        supervisor_result["assessment"]
    )

    st.header("5. Agricultural Knowledge Agent")
    st.write(knowledge_result["guidance"])