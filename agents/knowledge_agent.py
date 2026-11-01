
import ollama


def get_agricultural_guidance(
    question,
    assessment,
    crop_name=None,
    growth_stage=None,
    district=None,
    taluk=None,
    agro_climatic_zone=None,
    sowing_date=None
):
    """
    Generate farm-aware agricultural guidance using Ollama.
    Supports open-ended farmer questions and optional farm context.
    """

    farm_context = f"""
Crop: {crop_name or 'Not provided'}
Growth stage: {growth_stage or 'Not provided'}
District: {district or 'Not provided'}
Taluk: {taluk or 'Not provided'}
Agro-climatic zone: {agro_climatic_zone or 'Not provided'}
Sowing date: {sowing_date or 'Not provided'}
"""

    try:
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are AgriAgent, an agricultural decision-support "
                        "assistant. Answer farmers' questions clearly and "
                        "practically. Use the supplied farm context and crop "
                        "assessment when relevant. Provide general guidance "
                        "when information is missing, and clearly distinguish "
                        "general advice from facts supported by farm data. "
                        "Never invent satellite observations, weather "
                        "measurements, soil-test results, or farm conditions. "
                        "Ask for missing details when they materially affect "
                        "the recommendation. For pesticides, diseases, and "
                        "chemical treatments, recommend confirming the cause "
                        "and following local agricultural guidance and product "
                        "labels. Admit uncertainty when necessary."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Farmer's question:\n{question}\n\n"
                        f"Farm information:\n{farm_context}\n\n"
                        f"Available crop assessment:\n{assessment}\n\n"
                        "Provide practical guidance relevant to this farmer."
                    )
                }
            ]
        )

        guidance = response["message"]["content"].strip()

        return {
            "topic": "AI Agricultural Guidance",
            "assessment_context": assessment,
            "farm_context": farm_context,
            "guidance": guidance
        }

    except Exception as error:
        print(f"Local AI unavailable: {error}")

        return {
            "topic": "AI Agricultural Guidance",
            "assessment_context": assessment,
            "farm_context": farm_context,
            "guidance": (
                "The local AI assistant is currently unavailable. "
                "Please check that Ollama is running and the "
                "llama3.2:3b model is installed, then try again."
            )
        }
