"""
progress_manager.py
------------------
Manages user progress for Focus Zone tasks and skills.

This file provides functions to:
- Load existing progress from a JSON file (`progress.json`)
- Save progress to the JSON file
- Initialize/start a new skill plan for the user

Data stored in `progress.json` includes:
- skill: Name of the current skill being learned
- day: Current day in the skill plan
- unlocked_at: Timestamp when the current day's task was unlocked
- completed: List of completed tasks

Functions:
- load_progress() -> dict: Loads progress from file or returns default if not present
- save_progress(data: dict): Saves progress to file
- start_new_skill(skill: str) -> dict: Initializes a new skill plan and saves progress
"""
import json
import os
from datetime import datetime, timedelta

PROGRESS_FILE = "progress.json"

def load_progress():
    """Load existing user progress from file. Returns default progress if file not found."""
    if not os.path.exists(PROGRESS_FILE):
        return {"skill": None, "day": 0, "unlocked_at": None, "completed": []}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_progress(data):
    """Save user progress to file."""
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def start_new_skill(skill):
    """
    Initialize a new skill plan:
    - Sets day to 1
    - Sets unlocked_at to current timestamp
    - Clears completed tasks
    Returns the new progress dict.
    """
    progress = {
        "skill": skill,
        "day": 1,
        "unlocked_at": datetime.now().isoformat(),
        "completed": []
    }
    save_progress(progress)
    return progress
