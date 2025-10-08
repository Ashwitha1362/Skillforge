import json, os

def get_data_file(username):
    return f"skills_{username}.json"

def load_skills(username):
    file = get_data_file(username)
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

def save_skills(username, skills):
    file = get_data_file(username)
    with open(file, "w") as f:
        json.dump(skills, f, indent=4)
