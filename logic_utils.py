def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # Try numeric coercion first (handles strings that are numeric)
        try:
            gi = int(guess)
            si = int(secret)
            if gi == si:
                return "Win", "🎉 Correct!"
            if gi > si:
                return "Too High", "📉 Go LOWER!"
            return "Too Low", "📈 Go HIGHER!"
        except Exception:
            # Fallback to string comparison preserving correct hint semantics
            g = str(guess)
            s = str(secret)
            if g == s:
                return "Win", "🎉 Correct!"
            if g > s:
                return "Too High", "📉 Go LOWER!"
            return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return max(0, current_score + points)

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return max(0, current_score + 5)
        return max(0, current_score - 5)

    if outcome == "Too Low":
        return max(0, current_score - 5) #FIX: score now cannot go below 0

    return max(0, current_score)
