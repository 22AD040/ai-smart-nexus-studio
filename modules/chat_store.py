import json
import os

CHAT_DB = "data/chats.json"

def load_chats():
    if not os.path.exists(CHAT_DB):
        return []
    try:
        with open(CHAT_DB, "r") as f:
            return json.load(f)
    except:
        return []

def save_chat(entry):
    chats = load_chats()
    chats.append(entry)
    with open(CHAT_DB, "w") as f:
        json.dump(chats, f)