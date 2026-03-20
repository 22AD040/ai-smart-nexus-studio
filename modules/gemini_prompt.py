from google import genai
from config import get_gemini_key, GEMINI_MODEL

def generate_final_prompt(enhanced_prompt):
    try:
        client = genai.Client(api_key=get_gemini_key())

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=enhanced_prompt
        )

        return response.text if response.text else "Prompt generation failed"

    except Exception as e:
        return f"Error generating prompt: {str(e)}"