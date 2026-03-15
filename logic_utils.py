# FIX: Utilized AI to refactor the functions from app.py to logic_utils.py
def get_range_for_difficulty(difficulty: str): 
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal": # FIX: Swapped the ranges with "hard". Utilized AI to understand bug. 
        return 1, 50
    if difficulty == "Hard": # FIX: Swapped the ranges with "normal". Utilized AI to understand bug. 
        return 1, 100
    raise ValueError(f"Unknown difficulty: {difficulty!r}") # FIX: Raise error if unknown difficulty is input, rather than return a range. Utilized AI to understand bug and come up with solution for handling invalid values. 


def parse_guess(raw: str, low: int, high: int):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret): # FIX: Eliminated TypeError check since strings should not have been passed into this function in the first place. Utilized AI to understand information flow and brainstorm solution. 
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📈 Go LOWER!" # FIX: Fixed the message so it signals to go lower. Utilized AI to understand bug. 
    else:
        return "Too Low", "📉 Go HIGHER!" # FIX: Fixed the message so it signals to go higher. Utilized AI to understand bug. 


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score