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
