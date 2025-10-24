import json
import os

SCORE_FILE = "score_data.json"

def load_high_score():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r") as file:
                data = json.load(file)
                return data.get("high_score", 0)
        except (json.JSONDecodeError, ValueError):
            pass
    return 0 

def save_high_score(high_score):
    data = {"high_score": high_score}
    with open(SCORE_FILE, "w") as file:
        json.dump(data, file, indent=4)
