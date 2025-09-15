# generate_plan.py
import sys
import json

def generate_weekly_plan(skill, level):
    plan = {
        "Basic Cooking": [
            ("Monday", "Knife Skills: Safe Handling and Basic Cuts (dice, chop, mince)",
             ["Sharp knife", "cutting board", "onion", "potato", "carrot"],
             ["Knife", "cutting board", "bowl"]),
            ("Tuesday", "Understanding Cooking Temperatures: Boiling and Simmering",
             ["Pot", "water", "pasta (any kind)"],
             ["Pot", "stove", "timer", "measuring spoons"]),
            ("Wednesday", "Simple Egg Cooking: Scrambled, Fried, and Boiled",
             ["Eggs", "butter or oil", "salt", "pepper"],
             ["Frying pan", "saucepan", "whisk"]),
            ("Thursday", "Basic Salad Preparation: Washing, Chopping, and Dressing",
             ["Lettuce", "tomato", "cucumber", "vinaigrette dressing"],
             ["Cutting board", "knife", "bowl"]),
            ("Friday", "Cooking Rice: Perfect fluffy rice",
             ["Rice", "water", "pot with lid"],
             ["Pot with lid", "measuring cup"]),
            ("Saturday", "Simple One-Pan Meal: Roasted Vegetables",
             ["Broccoli", "carrots", "potatoes", "olive oil", "salt", "pepper"],
             ["Baking sheet", "oven"]),
            ("Sunday", "Review and Practice: Choose one task from this week and repeat it.",
             ["Ingredients from previous tasks"],
             ["Tools used in the chosen task"])
        ]
    }

    if skill not in plan:
        return {"error": "Skill not supported yet."}

    tasks = []
    unlock_time = 0  # Start immediately for the first task

    for day, task, requirements, tools in plan[skill]:
        tasks.append({
            "day": day,
            "task": task,
            "requirements": requirements,
            "tools": tools,
            "unlock_after": unlock_time
        })
        unlock_time = 24  # After the first one, always 24h delay

    return {
        "skill": skill,
        "level": level,
        "weekly_plan": tasks,
        "outcome": "Ability to perform basic cooking tasks and build confidence in the kitchen.",
        "next_step": "Learn more advanced cooking techniques like sautéing, stir-frying, and baking."
    }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_plan.py <skill> <level>")
    else:
        skill = sys.argv[1]
        level = sys.argv[2]
        plan = generate_weekly_plan(skill, level)
        print(json.dumps(plan, indent=2, ensure_ascii=False))
