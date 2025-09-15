import json
import time
import os
from datetime import datetime, timedelta
import google.generativeai as genai
import re

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
    """Load progress from file"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"current_day": 1, "last_completed": None}


def save_progress(progress):
    """Save progress to file"""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def run_focus_session(plan, avg_hours=2):
    """Run the focus zone session with timer + 3-question limit"""
    progress = load_progress()
    day = progress["current_day"]


    # find today's task
    todays_task = next((t for t in plan["weekly_plan"] if t["day"] == day), None)
    if not todays_task:
        print("✅ All tasks completed! You finished the weekly plan.")
        return

    # check if task is locked
    if progress["last_completed"]:
        last_done = datetime.fromisoformat(progress["last_completed"])
        unlock_time = last_done + timedelta(hours=todays_task["unlock_after"])
        if datetime.now() < unlock_time:
            wait = (unlock_time - datetime.now()).seconds // 3600
            print(f"⏳ Next task unlocks in {wait} hrs. Please come back later.")
            return

    # show task info
    print(f"\n📌 Focus Task - Day {todays_task['day']}")
    print(f"Task: {todays_task['task']}")
    print(f"Requirements: {', '.join(todays_task['requirements'])}")
    print(f"Tools: {', '.join(todays_task['tools'])}")
    print(f"⏱ You have {avg_hours:.1f} hours to complete this task.")

    # start timer (just simulates countdown in console)
    seconds = int(avg_hours * 3600)
    for remaining in range(seconds, 0, -1800):  # updates every 30 mins
        print(f"Time left: {remaining//3600}h {(remaining%3600)//60}m")
        time.sleep(1)  # ⬅️ change to 1800 for real 30-min updates

    print("\n⏰ Time is up! Great work on your task.")

    # AI help (limit 3 questions)
    help_count = 0
    while help_count < 3:
        q = input("Need AI help? (ask a question or type 'no'): ")
        if q.lower() == "no":
            break
        # here you'd call Gemini/OpenAI to answer, placeholder:
        print(f"🤖 AI: Here's a helpful tip for '{q}' ...")
        help_count += 1
    if help_count >= 3:
        print("⚠️ You reached the daily AI help limit.")

    # mark task complete
    progress["last_completed"] = datetime.now().isoformat()
    progress["current_day"] += 1
    save_progress(progress)
    print("✅ Task marked complete. Come back tomorrow for the next one!")

def safe_json_parse(text):
    """Strip markdown fences and parse JSON safely"""
    # Remove markdown ```json ... ``` wrappers if present
    cleaned = re.sub(r"```[a-zA-Z]*\n?", "", text).strip("` \n")
    try:
        return json.loads(cleaned)
    except Exception:
        return {"error": "Failed to parse AI response", "raw": text}
