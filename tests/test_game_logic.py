from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# BUG FIX TESTS: Test for reversed emoji messages bug
def test_guess_too_high_correct_hint_message():
    """When guess > secret, hint should say 'Go LOWER' not 'Go HIGHER'"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "📉" in message  # Should have down arrow, not up arrow

def test_guess_too_low_correct_hint_message():
    """When guess < secret, hint should say 'Go HIGHER' not 'Go LOWER'"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "📈" in message  # Should have up arrow, not down arrow

# BUG FIX TEST: Test for type mismatch bug (string vs integer comparison)
def test_guess_comparison_with_string_secret():
    """Comparing integer guess to integer secret should work correctly, not convert secret to string"""
    # Simulate the bug: if secret was converted to string, "60" > "50" would be True (lexicographic)
    # but 60 > 50 is also True (numeric), so test with a case where it matters
    outcome, message = check_guess(9, 50)
    # Numeric: 9 < 50 (Too Low) ✓
    # Lexicographic: "9" > "50" (Too High) ✗
    assert outcome == "Too Low", "Guess should use numeric comparison, not string comparison"
