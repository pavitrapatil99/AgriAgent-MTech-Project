import streamlit as st
import pandas as pd

from utils.karnataka_locations import (
    KARNATAKA_DISTRICTS,
    DISTRICT_TALUK_ZONES,
)
from agents.knowledge_agent import get_agricultural_guidance
from agents.satellite_agent import analyze_satellite
from agents.weather_agent import analyze_weather
from agents.supervisor_agent import generate_assessment

from utils.weather_api import get_hourly_forecast
from utils.weather_agent import get_combined_weather
from utils.crop_config import CROP_PROFILES, REGION_CONFIG


st.set_page_config(page_title="AgriAgent", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #f5f8f4; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
.main-header {
    background: linear-gradient(110deg, #174d32, #347c4c);
    padding: 28px; border-radius: 14px; color: white; margin-bottom: 25px;
}
.main-header h1 { color: white; margin-bottom: 5px; }
.main-header p { color: #e4f3e7; font-size: 16px; }
.section-header {
    color: #245c37; font-size: 22px; font-weight: 700;
    margin-top: 18px; margin-bottom: 12px;
}
div[data-testid="stMetric"] {
    background-color: white; border: 1px solid #e0e9df;
    padding: 15px; border-radius: 12px;
}
.stButton > button {
    background-color: #267343; color: white; border-radius: 8px;
    border: none; padding: 8px 18px;
}
.stButton > button:hover { background-color: #174d32; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🌱 AgriAgent</h1>
    <p>Intelligent Agricultural Decision Support Using Satellite, Weather and AI Agent Technology</p>
</div>
""", unsafe_allow_html=True)

st.write("Welcome to AgriAgent. Enter your farm details to analyze crop conditions and receive agricultural guidance.")

# 1. Farm location
st.markdown('<div class="section-header">📍 1. Farm Location</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.text_input("State", value=REGION_CONFIG["state"], disabled=True)
with col2:
    default_district = REGION_CONFIG["district"]
    district_index = KARNATAKA_DISTRICTS.index(default_district) if default_district in KARNATAKA_DISTRICTS else 0
    selected_district = st.selectbox("Select District", KARNATAKA_DISTRICTS, index=district_index)

available_taluks = list(DISTRICT_TALUK_ZONES.get(selected_district, {}).keys())
if available_taluks:
    selected_area = st.selectbox("Select Taluk", available_taluks, key=f"taluk_selection_{selected_district}")
    selected_zone = DISTRICT_TALUK_ZONES[selected_district][selected_area]
    st.text_input("Agro-Climatic Zone", value=selected_zone, disabled=True)
else:
    selected_area = None
    selected_zone = "Mapping Pending"
    st.warning(f"Taluk and agro-climatic zone mapping for {selected_district} is pending verification.")

# 2. Crop information
st.markdown('<div class="section-header">🌾 2. Crop Information</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    crop_name = st.selectbox("Select Crop", list(CROP_PROFILES.keys()))
with col2:
    growth_stage = st.selectbox("Current Growth Stage", CROP_PROFILES[crop_name]["stages"])

col1, col2 = st.columns(2)
with col1:
    stage_method = st.selectbox("Growth Stage Selection Method", ["Manual Selection", "Automatic Estimation"])
with col2:
    sowing_date = st.date_input("Crop Sowing Date")
if stage_method == "Automatic Estimation":
    st.info("Automatic growth-stage estimation will be enabled after crop-specific duration profiles are validated. For now, please select the stage manually.")

# 3. Satellite information
st.markdown('<div class="section-header">🛰️ 3. Satellite Information</div>', unsafe_allow_html=True)
with st.container(border=True):
    st.caption("Enter the available vegetation reading. Live satellite processing is a planned integration.")
    ndvi = st.slider("Vegetation Indicator (NDVI)", min_value=-1.0, max_value=1.0, value=0.45, step=0.05)

# 4. Weather information
st.markdown('<div class="section-header">🌦️ 4. Weather Information</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    rainfall = st.number_input("Manual Rainfall (mm)", min_value=0.0, max_value=500.0, value=5.0, step=1.0)
with col2:
    temperature = st.number_input("Manual Temperature (°C)", min_value=-10.0, max_value=60.0, value=32.0, step=1.0)

# 5. Historical and forecast weather
st.markdown('<div class="section-header">📊 5. Historical and Forecast Weather</div>', unsafe_allow_html=True)
if st.button("Fetch Historical and Forecast Weather"):
    try:
        combined_weather = get_combined_weather()
        st.session_state["combined_weather"] = combined_weather
        st.success("Historical and forecast weather retrieved successfully!")
    except Exception as error:
        st.error(f"Weather retrieval failed: {error}")

if "combined_weather" in st.session_state:
    combined_weather = st.session_state["combined_weather"]
    historical = combined_weather[combined_weather["data_type"] == "Historical"]
    forecast = combined_weather[combined_weather["data_type"] == "Forecast"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Historical Rainfall", f"{historical['rainfall'].sum():.1f} mm")
    c2.metric("Forecast Rainfall", f"{forecast['rainfall'].sum():.1f} mm")
    c3.metric("Historical Temperature", f"{historical['temperature'].mean():.1f} °C")
    c4.metric("Forecast Temperature", f"{forecast['temperature'].mean():.1f} °C")
    with st.expander("View Complete Weather Data"):
        st.dataframe(combined_weather, use_container_width=True)

# Live hourly weather
with st.expander("🌤️ View Live Hourly Weather Forecast"):
    if st.button("Fetch Hourly Forecast"):
        try:
            forecast_data = get_hourly_forecast()
            hourly = forecast_data["hourly"]
            forecast_df = pd.DataFrame({
                "Time": hourly["time"],
                "Temperature (°C)": hourly["temperature_2m"],
                "Humidity (%)": hourly["relative_humidity_2m"],
                "Precipitation (mm)": hourly["precipitation"],
            })
            st.success("Hourly forecast retrieved successfully!")
            st.dataframe(forecast_df.head(24), use_container_width=True)
        except Exception as error:
            st.error(f"Could not fetch forecast: {error}")

# 6. Farmer question
st.markdown('<div class="section-header">💬 6. Ask AgriAgent</div>', unsafe_allow_html=True)
farmer_question = st.text_input("Enter your agricultural question", placeholder="Example: Why are my paddy leaves turning yellow?")

# 7. AI agent analysis
st.markdown('<div class="section-header">🤖 7. AI Agent Analysis</div>', unsafe_allow_html=True)
if st.button("Analyze Crop Conditions", use_container_width=True):
    try:
        with st.status("Analyzing crop conditions...", expanded=True) as status:
            st.write("Running Satellite Agent...")
            satellite_result = analyze_satellite(ndvi)
            st.write("Satellite Agent completed.")

            st.write("Running Weather Agent...")
            weather_result = analyze_weather(rainfall, temperature)
            st.write("Weather Agent completed.")

            st.write("Running Supervisor Agent...")
            supervisor_result = generate_assessment(satellite_result, weather_result)
            st.write("Supervisor Agent completed.")

            st.write("Connecting to Ollama Knowledge Agent...")
            knowledge_result = get_agricultural_guidance(
                question=farmer_question,
                assessment=supervisor_result["assessment"],
                crop_name=crop_name,
                growth_stage=growth_stage,
                district=selected_district,
                taluk=selected_area,
                agro_climatic_zone=selected_zone,
                sowing_date=str(sowing_date),
            )
            st.write("Ollama response received.")

            st.session_state["analysis_results"] = {
                "satellite": satellite_result,
                "weather": weather_result,
                "supervisor": supervisor_result,
                "knowledge": knowledge_result,
            }
            status.update(label="Crop analysis completed successfully!", state="complete")
    except Exception as error:
        st.error(f"Analysis failed: {error}")

# 8. Display results
if "analysis_results" in st.session_state:
    results = st.session_state["analysis_results"]
    st.markdown('<div class="section-header">📋 8. Analysis Results</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("🛰️ Satellite Agent")
            st.metric("NDVI", results["satellite"]["ndvi"])
            st.write(results["satellite"]["condition"])
    with col2:
        with st.container(border=True):
            st.subheader("🌦️ Weather Agent")
            st.metric("Rainfall", f"{results['weather']['rainfall_mm']} mm")
            st.metric("Temperature", f"{results['weather']['temperature_c']} °C")
            st.write(results["weather"]["assessment"])

    st.subheader("🧠 Supervisor Agent")
    with st.container(border=True):
        st.write(results["supervisor"]["assessment"])
        st.subheader("Recommended Next Steps")
        st.write(results["supervisor"]["recommendation"])

    st.subheader("📚 Agricultural Knowledge Agent")
    with st.container(border=True):
        st.write(results["knowledge"]["guidance"])

    st.warning("These results are preliminary indicators, not a confirmed crop diagnosis. Verify field conditions and soil moisture before making agricultural decisions.")

# Footer
st.divider()
st.caption("AgriAgent | M.Tech AIML Project | Agricultural Decision Support System")