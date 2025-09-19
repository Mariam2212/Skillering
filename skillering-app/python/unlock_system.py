"""
unlock_system.py
----------------
Manages the unlocking and completion of daily tasks in the Focus Zone project.

This file:
- Checks if the current day's task is unlocked based on time and user progress.
- Marks tasks as completed, updating:
    - Current day
    - List of completed tasks
    - Next unlock timestamp (24 hours after completion)
- Relies on `progress_manager` to load and save user progress.
- Provides two main functions:
    1. `is_task_unlocked()` → Returns a tuple (bool, message) indicating if the task is available.
    2. `complete_task()` → Marks the current task as complete and schedules the next unlock.
"""

from datetime import datetime, timedelta
from progress_manager import load_progress, save_progress

def is_task_unlocked():
    progress = load_progress()
    if not progress["skill"]:
        return False, "❌ No skill selected."

    unlocked_at = datetime.fromisoformat(progress["unlocked_at"])
    if datetime.now() >= unlocked_at:
        return True, f"✅ Task {progress['day']} is unlocked."
    else:
        hours_left = (unlocked_at - datetime.now()).seconds // 3600
        return False, f"⏳ Task locked. Try again in {hours_left}h."

def complete_task():
    progress = load_progress()
    if not progress["skill"]:
        return {"error": "No skill started."}

    progress["completed"].append(progress["day"])
    progress["day"] += 1
    progress["unlocked_at"] = (datetime.now() + timedelta(hours=24)).isoformat()
    save_progress(progress)
    return {"success": f"Task completed. Next unlock: {progress['unlocked_at']}"}
