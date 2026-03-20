import google.generativeai as genai
from config import get_gemini_key, GEMINI_MODEL


def generate_final_prompt(enhanced_prompt):
    try:
        genai.configure(api_key=get_gemini_key())

        model = genai.GenerativeModel(GEMINI_MODEL)

        response = model.generate_content(enhanced_prompt)

        return response.text if response.text else "Prompt generation failed"

    except Exception as e:
        return f"Error generating prompt: {str(e)}"