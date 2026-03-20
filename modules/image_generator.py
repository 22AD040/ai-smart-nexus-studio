import requests
from config import get_api_key


HF_API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

def generate_image(prompt):
    try:
        api_key = get_api_key()

        if not api_key:
            print("❌ No API key found")
            return None

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "inputs": prompt
        }

        response = requests.post(HF_API_URL, headers=headers, json=payload)

        print("STATUS:", response.status_code)

        if response.status_code == 200:
            return response.content

        elif response.status_code == 503:
            print("⏳ Model loading... try again")
            return None

        else:
            print("❌ ERROR:", response.text)
            return None

    except Exception as e:
        print("❌ EXCEPTION:", str(e))
        return None