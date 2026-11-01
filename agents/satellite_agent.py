
def analyze_satellite(ndvi):
    """
    Analyze the vegetation condition using an NDVI value.
    NDVI is an indicator, not a definitive crop diagnosis.
    """

    if ndvi >= 0.6:
        condition = "Healthy vegetation indicator"
    elif ndvi >= 0.3:
        condition = "Moderate vegetation indicator"
    else:
        condition = "Low vegetation indicator"

    return {
        "ndvi": ndvi,
        "condition": condition
    }
