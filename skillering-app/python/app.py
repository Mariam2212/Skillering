"""
app.py
--------
Main FastAPI entry point for the Focus Zone AI backend.

This file:
- Creates the FastAPI application instance.
- Exposes API endpoints for:
  - Root health check (`/`)
  - Screen time analysis & skill suggestions (`/analysis`)
  - Generating a 7-day Focus Zone learning plan (`/focus-plan/{skill}/{level}`)
  - Running focus sessions (`/focus-session/{minutes}`)
  - Managing user progress:
      - Load progress (`/progress/load`)
      - Start a new skill plan (`/progress/start/{skill}`)
  - Unlock system for tasks:
      - Check if task unlocked (`/task/unlock`)
      - Mark task complete (`/task/complete`)
  - Skills suggestions (`/skills/suggest`)
- Uses helper modules:
  - `utils` → API setup (e.g., Gemini/OpenAI keys)
  - `screentime` → Load & analyze screen time data
  - `skills` → Suggest offline skills
  - `focus_zone` → Generate learning plans & manage sessions
  - `progress_manager` → Load/save progress and start new skills
  - `unlock_system` → Task unlock and completion logic
"""

from fastapi import FastAPI, File, UploadFile
from utils import setup_api
from screentime import load_screentime, calculate_average_hours, save_screentime, daily_average
from skills import suggest_skills
from focus_zone import generate_focus_plan, run_focus_session
from progress_manager import load_progress, start_new_skill
import pandas as pd
from fastapi import Body
from unlock_system import is_task_unlocked, complete_task

# ----------------- App Setup ----------------- #
app = FastAPI(
    title="Focus Zone AI Backend",
    description="Provides endpoints for Focus Zone project",
    version="1.2.0"
)

# ✅ Setup external API (Gemini or other integrations)
setup_api()

# ----------------- Root ----------------- #
@app.get("/")
def root():
    return {"status": "ok", "message": "Focus Zone AI backend is running 🚀"}

# ----------------- Analysis ----------------- #
@app.get("/analysis")
def analyze():
    try:
        df = load_screentime()
        avg_hours = calculate_average_hours(df)
        skills = suggest_skills(avg_hours)
        return {"status": "success", "average_hours": avg_hours, "suggested_skills": skills}
    except Exception as e:
        return {"status": "error", "details": str(e)}

# ----------------- Focus Plan / Session ----------------- #
@app.get("/focus-plan/{skill}/{level}")
def focus_plan(skill: str, level: str = "beginner"):
    try:
        plan = generate_focus_plan(skill, level)
        return {"status": "success", "skill": skill, "level": level, "plan": plan}
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.get("/focus-session/{minutes}")
def focus_session(minutes: int):
    try:
        session = run_focus_session(minutes)
        return {"status": "success", "minutes": minutes, "session": session}
    except Exception as e:
        return {"status": "error", "details": str(e)}

# ----------------- Progress ----------------- #
@app.get("/progress/load")
def get_progress():
    """Load current user progress."""
    try:
        progress = load_progress()
        return {"status": "success", "progress": progress}
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.post("/progress/start/{skill}")
def start_skill(skill: str):
    """Start a new skill plan."""
    try:
        progress = start_new_skill(skill)
        return {"status": "success", "progress": progress}
    except Exception as e:
        return {"status": "error", "details": str(e)}

# ----------------- Screen Time ----------------- #
@app.post("/screentime/upload")
async def upload_screentime(file: UploadFile = File(...)):
    """Upload a new screentime CSV file, replacing existing data."""
    try:
        df = pd.read_csv(file.file)
        save_screentime(df)
        return {"status": "success", "message": "File uploaded successfully"}
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.get("/screentime/daily-averages")
def get_daily_averages():
    """Return average screen time per day in hours."""
    try:
        df = load_screentime()
        averages = daily_average(df)
        return {"status": "success", "daily_averages": averages}
    except Exception as e:
        return {"status": "error", "details": str(e)}

# ----------------- Skills ----------------- #
@app.post("/skills/suggest")
def suggest_skills_endpoint(
    avg_hours: float = Body(..., embed=True),
    usage: dict = Body(None, embed=True)
):
    """
    Suggest 3 skills based on user screentime and app usage.
    Request body example:
    {
        "avg_hours": 3.5,
        "usage": {
            "YouTube": 1.5,
            "TikTok": 0.5,
            "Discord": 1.0
        }
    }
    Response JSON:
    [
        {"skill": "...", "level": "...", "why": "...", "category": "..."},
        ...
    ]
    """
    try:
        skills = suggest_skills(avg_hours, usage)
        return {"status": "success", "skills": skills}
    except Exception as e:
        return {"status": "error", "details": str(e)}

# ---------------- Unlock System ---------------- #
@app.get("/task/unlock")
def check_task_unlock():
    """
    Check if the current day's task is unlocked.
    Returns:
    {
        "status": "success",
        "unlocked": True/False,
        "message": "..."
    }
    """
    try:
        unlocked, message = is_task_unlocked()
        return {"status": "success", "unlocked": unlocked, "message": message}
    except Exception as e:
        return {"status": "error", "details": str(e)}


@app.post("/task/complete")
def mark_task_complete():
    """
    Mark the current task as complete.
    Updates day count and sets next unlock time (24h later).
    Returns:
    {
        "status": "success",
        "message": "..."
    }
    """
    try:
        result = complete_task()
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {"status": "success", "message": result["success"]}
    except Exception as e:
        return {"status": "error", "details": str(e)}
