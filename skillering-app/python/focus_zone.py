import json
import os
import re
from datetime import datetime, timedelta
import google.generativeai as genai

PROGRESS_FILE = "progress.json"


def generate_focus_plan(skill, level):
    prompt = f"""
    Create a **7-day Focus Zone plan** for learning "{skill}" at {level} level.
    Each day = 1 microtask.
    Each microtask must include:
      - "day"
      - "task"
      - "requirements"
      - "tools"
      - "unlock_after" (hours after previous task, usually 24)

    Return as JSON with format:
    {{
        "skill": "{skill}",
        "level": "{level}",
        "weekly_plan": [...],
        "outcome": "...",
        "next_step": "..."
    }}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    try:
        return safe_json_parse(response.text)
    except:
        return {"error": "Failed to parse AI response", "raw": response.text}


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"current_day": 1, "last_completed": None}


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def run_focus_session(plan, avg_hours=2):
    """
    Run focus session (API-friendly version).
    Instead of sleeping/printing, return JSON for frontend.
    """
    progress = load_progress()
    day = progress["current_day"]

    # find today's task
    todays_task = next((t for t in plan.get("weekly_plan", []) if t["day"] == day), None)
    if not todays_task:
        return {"status": "done", "message": "All tasks completed! 🎉"}

    # check if task is locked
    if progress["last_completed"]:
        last_done = datetime.fromisoformat(progress["last_completed"])
        unlock_time = last_done + timedelta(hours=todays_task["unlock_after"])
        if datetime.now() < unlock_time:
            wait = (unlock_time - datetime.now()).seconds // 3600
            return {
                "status": "locked",
                "message": f"Next task unlocks in {wait} hrs ⏳"
            }

    # return session data (let frontend handle timer)
    return {
        "status": "active",
        "day": todays_task["day"],
        "task": todays_task["task"],
        "requirements": todays_task["requirements"],
        "tools": todays_task["tools"],
        "time_allocated": avg_hours,
    }


def complete_task():
    """Mark current task complete"""
    progress = load_progress()
    progress["last_completed"] = datetime.now().isoformat()
    progress["current_day"] += 1
    save_progress(progress)
    return {"status": "success", "message": "Task marked complete ✅"}


def safe_json_parse(text):
    """Strip markdown fences and parse JSON safely"""
    cleaned = re.sub(r"```[a-zA-Z]*\n?", "", text).strip("` \n")
    try:
        return json.loads(cleaned)
    except Exception:
        return {"error": "Failed to parse AI response", "raw": text}
