import streamlit as st
import os
import uuid

IMAGE_DIR = "data/images"

os.makedirs(IMAGE_DIR, exist_ok=True)

def save_image(image_bytes):
    filename = f"{uuid.uuid4()}.png"
    path = os.path.join(IMAGE_DIR, filename)

    with open(path, "wb") as f:
        f.write(image_bytes)

    return path