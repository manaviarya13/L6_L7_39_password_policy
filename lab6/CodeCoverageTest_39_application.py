
import pytest

from password_policy import check_password, strength, suggest_fix


# -------------------------------
# CHECK_PASSWORD TEST CASES
# -------------------------------

def test_valid_password():
    assert check_password("Abcdef1!") == []


def test_password_too_short():
    assert "too short" in check_password("Ab1!")


def test_password_too_long():
    assert "too long" in check_password("A" * 65)


def test_password_length_boundary_minimum():
    assert "too short" not in check_password("Abcde1!X")


def test_password_length_boundary_maximum():
    assert "too long" not in check_password("A" * 64)


def test_common_password():
    assert "common" in check_password("password")


def test_common_password_case_insensitive():
    assert "common" in check_password("PASSWORD")


def test_missing_uppercase():
    assert "no uppercase" in check_password("abcdef1!")


def test_missing_lowercase():
    assert "no lowercase" in check_password("ABCDEF1!")


def test_missing_digit():
    assert "no digit" in check_password("Abcdefgh!")


def test_missing_special_character():
    assert "no special" in check_password("Abcdef12")


def test_password_missing_multiple_character_types():
    issues = check_password("abcdefgh")
    assert "no uppercase" in issues
    assert "no digit" in issues
    assert "no special" in issues


def test_password_with_all_character_types():
    assert check_password("Secure123!") == []


# -------------------------------
# STRENGTH TEST CASES
# -------------------------------

def test_strong_password():
    assert strength("SecurePassword123!") == "strong"


def test_good_password():
    assert strength("Abcdef1!") == "good"


def test_weak_password():
    assert strength("abcdefg!") == "weak"


def test_very_weak_password():
    assert strength("abc") == "very weak"


def test_good_password_at_length_14():
    assert strength("Abcdefgh1234!X") == "strong"


# -------------------------------
# SUGGEST_FIX TEST CASES
# -------------------------------

def test_no_fix_needed():
    assert suggest_fix([]) == "none needed"


def test_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_fix_common_password():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_fix_no_uppercase():
    assert suggest_fix(["no uppercase"]) == "add uppercase"


def test_fix_no_lowercase():
    assert suggest_fix(["no lowercase"]) == "add lowercase"


def test_fix_no_digit():
    assert suggest_fix(["no digit"]) == "add digit"


def test_fix_no_special():
    assert suggest_fix(["no special"]) == "add special"


def test_fix_too_long():
    assert suggest_fix(["too long"]) == "shorten it"


def test_fix_unknown_issue():
    assert suggest_fix(["unknown issue"]) == "shorten it"


def test_first_issue_is_used():
    assert suggest_fix(
        ["too short", "no uppercase"]
    ) == "add more characters"
