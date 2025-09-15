import json
import os
from datetime import datetime, timedelta

PROGRESS_FILE = "progress.json"

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {"skill": None, "day": 0, "unlocked_at": None, "completed": []}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_progress(data):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def start_new_skill(skill):
    progress = {
        "skill": skill,
        "day": 1,
        "unlocked_at": datetime.now().isoformat(),
        "completed": []
    }
    save_progress(progress)
    return progress
