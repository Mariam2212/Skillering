def regenerate_skills(avg_hours, feedback, num_skills=3):
    if avg_hours <= 2:
        level = "Beginner"
    elif 2 < avg_hours <= 5:
        level = "Intermediate"
    else:
        level = "Advanced"

    prompt = f"""
    The user spends {avg_hours:.1f} hours daily on apps.
    They gave this feedback on previous skills: "{feedback}".
    Suggest {num_skills} offline skills for them at the **{level} level**,
    taking feedback into account (e.g., harder skills if they said "too easy").
    Return JSON list:
    [{{"skill":"...","level":"{level}","why":"..."}}]
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    try:
        return safe_json_parse(response.text)
    except:
        return {"error": "Failed to parse AI response", "raw": response.text}
