import os
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

GEMINI_MODEL = "gemini-2.5-flash"

def get_gemini_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except:
        return os.getenv("GEMINI_API_KEY")

def get_api_key():
    try:
        return st.secrets["HF_API_KEY"]
    except:
        return os.getenv("HF_API_KEY")