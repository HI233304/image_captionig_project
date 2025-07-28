import json
import os
import hashlib
import random

USERS_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)
    return True

def check_login(username, password):
    users = load_users()
    hashed = hash_password(password)
    return username in users and users[username]["password"] == hashed

def register_user(username, password, email):
    users = load_users()
    if username in users:
        return "exists"
    if len(password) < 6:
        return "weak"
    if "@" not in email or "." not in email:
        return "invalid_email"
    users[username] = {
        "password": hash_password(password),
        "email": email,
        "otp": ""
    }
    save_users(users)
    return "ok"

def generate_otp(username):
    users = load_users()
    if username not in users:
        return None
    otp = str(random.randint(100000, 999999))
    users[username]["otp"] = otp
    save_users(users)
    return otp

def reset_password(username, otp, new_password):
    users = load_users()
    if username not in users:
        return "not_found"
    if users[username].get("otp") != otp:
        return "invalid_otp"
    users[username]["password"] = hash_password(new_password)
    users[username]["otp"] = ""
    save_users(users)
    return "ok"