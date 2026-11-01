
import os
from openai import OpenAI

if not os.getenv("OPENAI_API_KEY"):
    print("API key not found. Set OPENAI_API_KEY in this Command Prompt.")
else:
    try:
        client = OpenAI()

        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=(
                "You are an agricultural assistant. Give clear, practical "
                "guidance to farmers. Do not claim certainty without evidence. "
                "For pesticide, disease, or fertilizer advice, mention that "
                "recommendations depend on crop, location, and local guidance."
            ),
            input=(
                "How can a farmer improve soil health before planting "
                "tomatoes? Give five practical steps."
            ),
        )

        print("\nAI answer:\n")
        print(response.output_text)

    except Exception as error:
        print("AI test failed:", error)
