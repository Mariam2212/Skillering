"""
skills.py
----------
Provides functionality to suggest offline and practical skills for users based on
their screen time and app usage patterns.

This file:
- Uses AI (Gemini) to generate skill recommendations.
- Determines user skill level based on average daily screen time:
    - <=2 hours → Beginner
    - 2–5 hours → Intermediate
    - >5 hours → Advanced
- Suggests exactly 3 skills:
    1. Practical life skill
    2. Non-digital offline hobby
    3. Money-making skill
- Each suggested skill includes:
    - "skill": name of the skill
    - "level": recommended skill level
    - "why": reason it’s suggested
    - "category": type of skill (practical, non-digital, money-making)
- Uses `safe_json_parse` to safely parse AI JSON output.
"""

import json
import google.generativeai as genai
import re

def suggest_skills(avg_hours, usage=None):
    """
    Suggest 3 skills based on user screentime and app usage.
    - One practical life skill
    - One non-digital offline hobby
    - One money-making skill
    """

    if avg_hours <= 2:
        level = "Beginner"
    elif 2 < avg_hours <= 5:
        level = "Intermediate"
    else:
        level = "Advanced"

    usage_text = json.dumps(usage, indent=2, ensure_ascii=False) if usage else "No app usage data"

    prompt = f"""
    The user spends {avg_hours:.1f} hours daily on apps.
    Here is their app usage (hours per day):
    {usage_text}

    Based on this:
    - Suggest exactly 3 skills.
    - One must be a PRACTICAL life skill.
    - One must be a NON-DIGITAL offline hobby.
    - One must be a MONEY-MAKING skill.
    - Match each skill to the {level} level.
    - Each skill should have: "skill", "level", "why", and "category" (practical, non-digital, money-making).

    Return ONLY valid JSON array:
    [
      {{"skill": "...", "level": "{level}", "why": "...", "category": "practical"}},
      {{"skill": "...", "level": "{level}", "why": "...", "category": "non-digital"}},
      {{"skill": "...", "level": "{level}", "why": "...", "category": "money-making"}}
    ]
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    try:
        return safe_json_parse(response.text)
    except:
        return {"error": "Failed to parse AI response", "raw": response.text}

def safe_json_parse(text):
    """Strip markdown fences and parse JSON safely"""
    cleaned = re.sub(r"```[a-zA-Z]*\n?", "", text).strip("` \n")
    try:
        return json.loads(cleaned)
    except Exception:
        return {"error": "Failed to parse AI response", "raw": text}
