from password_policy import check_password, strength, suggest_fix


# Password length branches
def test_password_too_short():
    assert "too short" in check_password("Ab1!")


def test_password_valid_length():
    assert "too short" not in check_password("Abcdef1!")


def test_password_too_long():
    assert "too long" in check_password("A" * 65)


def test_password_maximum_length():
    assert "too long" not in check_password("A" * 64)


# Common password branches
def test_common_password():
    assert "common" in check_password("password")


def test_not_common_password():
    assert "common" not in check_password("Secure123!")


# Character type branches
def test_uppercase_present():
    assert "no uppercase" not in check_password("Abcdef1!")


def test_uppercase_missing():
    assert "no uppercase" in check_password("abcdef1!")


def test_lowercase_present():
    assert "no lowercase" not in check_password("ABCdef1!")


def test_lowercase_missing():
    assert "no lowercase" in check_password("ABCDEF1!")


def test_digit_present():
    assert "no digit" not in check_password("Abcdef1!")


def test_digit_missing():
    assert "no digit" in check_password("Abcdefgh!")


def test_special_present():
    assert "no special" not in check_password("Abcdef1!")


def test_special_missing():
    assert "no special" in check_password("Abcdef12")


# Strength classification branches
def test_strong_password():
    assert strength("SecurePassword123!") == "strong"


def test_good_password():
    assert strength("Abcdef1!") == "good"


def test_weak_password():
    assert strength("abcdefg!") == "weak"


def test_very_weak_password():
    assert strength("abc") == "very weak"


# Suggestion branches
def test_no_fix_needed():
    assert suggest_fix([]) == "none needed"


def test_fix_short_password():
    assert suggest_fix(["too short"]) == "add more characters"


def test_fix_common_password():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_fix_uppercase():
    assert suggest_fix(["no uppercase"]) == "add uppercase"


def test_fix_lowercase():
    assert suggest_fix(["no lowercase"]) == "add lowercase"


def test_fix_digit():
    assert suggest_fix(["no digit"]) == "add digit"


def test_fix_special():
    assert suggest_fix(["no special"]) == "add special"


def test_fix_fallback():
    assert suggest_fix(["too long"]) == "shorten it"