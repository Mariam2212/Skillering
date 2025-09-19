

from fastapi import FastAPI
from utils import setup_api
from screentime import load_screentime, calculate_average_hours
from skills import suggest_skills
from focus_zone import generate_focus_plan, run_focus_session
from generate_plan import generate_weekly_plan  # ⬅ import the module

# ✅ Create FastAPI app
app = FastAPI(
    title="Focus Zone AI Backend",
    description="Provides endpoints for Focus Zone project",
    version="1.1.0"
)

# ✅ Setup external API (Gemini or other integrations)
setup_api()


@app.get("/")
def root():
    return {"status": "ok", "message": "Focus Zone AI backend is running 🚀"}


@app.get("/analysis")
def analyze():
    try:
        df = load_screentime()
        avg_hours = calculate_average_hours(df)
        skills = suggest_skills(avg_hours)
        return {"status": "success", "average_hours": avg_hours, "suggested_skills": skills}
    except Exception as e:
        return {"status": "error", "details": str(e)}


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


# ✅ NEW endpoint to generate weekly plan from generate_plan.py
@app.get("/generate-plan/{skill}/{level}")
def generate_plan(skill: str, level: str = "beginner"):
    """
    Generate a structured weekly plan using generate_plan.py.
    Frontend/backend can call this to get tasks for a specific skill.
    """
    try:
        plan = generate_weekly_plan(skill, level)
        return {"status": "success", "plan": plan}
    except Exception as e:
        return {"status": "error", "details": str(e)}
