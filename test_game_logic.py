import pytest
from logic_utils import get_range_for_difficulty, parse_guess, check_guess


# --- Bug 1: Difficulty ranges and attempts did not scale correctly ---

def test_easy_range_is_smallest():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range_is_medium():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_range_is_largest():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_ranges_increase_with_difficulty():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high

def test_unknown_difficulty_raises_error():
    with pytest.raises(ValueError):
        get_range_for_difficulty("Impossible")


# --- Bug 2: Guesses outside the valid range did not produce an error ---

def test_guess_below_range_is_invalid():
    ok, _, err = parse_guess("0", 1, 20)
    assert ok is False
    assert err is not None

def test_guess_above_range_is_invalid():
    ok, _, err = parse_guess("21", 1, 20)
    assert ok is False
    assert err is not None

def test_guess_at_lower_bound_is_valid():
    ok, value, err = parse_guess("1", 1, 20)
    assert ok is True
    assert value == 1

def test_guess_at_upper_bound_is_valid():
    ok, value, err = parse_guess("20", 1, 20)
    assert ok is True
    assert value == 20


# --- Bug 3: Hints were backwards (go lower/higher were swapped) ---

def test_hint_says_go_lower_when_guess_is_too_high():
    outcome, message = check_guess(15, 10)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_says_go_higher_when_guess_is_too_low():
    outcome, message = check_guess(5, 10)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_correct_guess_returns_win():
    outcome, _ = check_guess(10, 10)
    assert outcome == "Win"