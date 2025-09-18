import json
from fastapi import FastAPI
from utils import setup_api
from screentime import load_screentime, calculate_average_hours
from skills import suggest_skills
from focus_zone import generate_focus_plan, run_focus_session

# ✅ Create FastAPI app
app = FastAPI()

# ✅ Setup API (Gemini or other integrations)
setup_api()

@app.get("/")
def root():
    return {"message": "Focus Zone AI backend is running 🚀"}

@app.get("/analysis")
def analyze():
    """
    Endpoint that loads screentime data, calculates averages,
    suggests offline skills, and returns JSON for the frontend.
    """
    df = load_screentime()
    avg_hours = calculate_average_hours(df)

    skills = suggest_skills(avg_hours)
    if "error" in skills:
        return skills

    return {
        "average_hours": avg_hours,
        "suggested_skills": skills
    }

@app.get("/focus-plan/{skill}/{level}")
def focus_plan(skill: str, level: str):
    """
    Generate a 7-day Focus Zone plan.
    """
    return generate_focus_plan(skill, level)

@app.get("/focus-session/{minutes}")
def focus_session(minutes: int):
    """
    Run a focus session for given minutes.
    """
    return run_focus_session(minutes)
