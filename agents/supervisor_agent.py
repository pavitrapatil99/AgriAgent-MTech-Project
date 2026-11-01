
def generate_assessment(satellite_result, weather_result):
    """
    Combine satellite and weather indicators into a preliminary assessment.
    This is a simple rule-based supervisor, not an ML model.
    """

    ndvi = satellite_result["ndvi"]
    rainfall = weather_result["rainfall_mm"]
    temperature = weather_result["temperature_c"]

    if ndvi < 0.3 and rainfall < 10 and temperature > 30:
        assessment = (
            "Possible crop stress: low vegetation indicator, "
            "low rainfall, and high temperature."
        )
        recommendation = (
            "Check soil moisture, irrigation availability, and crop condition."
        )

    elif ndvi < 0.3:
        assessment = (
            "Low vegetation indicator detected. The cause is not yet confirmed."
        )
        recommendation = (
            "Inspect the crop and check soil moisture and possible pest or nutrient issues."
        )

    elif rainfall < 10 and temperature > 30:
        assessment = (
            "Weather conditions may increase the risk of water stress."
        )
        recommendation = (
            "Monitor soil moisture and review the crop's irrigation requirements."
        )

    else:
        assessment = (
            "The available indicators do not show a clear combined stress signal."
        )
        recommendation = (
            "Continue monitoring crop and weather conditions."
        )

    return {
        "assessment": assessment,
        "recommendation": recommendation
    }
