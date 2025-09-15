import json
from utils import setup_api
from screentime import load_screentime, calculate_average_hours
from skills import suggest_skills
from focus_zone import generate_focus_plan, run_focus_session

# Setup API
setup_api()

df = load_screentime()
avg_hours = calculate_average_hours(df)

skills = suggest_skills(avg_hours)
if "error" in skills:
    print(json.dumps(skills, ensure_ascii=False, indent=2))
    exit()

# ✅ Output skills in JSON (so frontend can render bubbles)
print(json.dumps({
    "average_hours": avg_hours,
    "suggested_skills": skills
}, ensure_ascii=False, indent=2))
