import json
import os
import hashlib  

USER_DB = "data/users.json"


def load_users():
    if not os.path.exists(USER_DB):
        return {}

    try:
        with open(USER_DB, "r") as f:
            return json.load(f)
    except:
        return {}


def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f)



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def register_user(username, password, full_name):
    users = load_users()

    if username in users:
        return False

    users[username] = {
        "password": hash_password(password),  # 🔐 hashed
        "full_name": full_name
    }

    save_users(users)
    return True



def login_user(username, password):
    users = load_users()

    if username in users:
        
        if users[username]["password"] == hash_password(password):
            return users[username]

    return None