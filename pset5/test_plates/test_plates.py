from plates import is_valid


def test_single_character():
    assert is_valid("H") == False


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True


def test_invalid_plates():
    assert is_valid("CS05") == False # Checks for zero placement
    assert is_valid("CS50P2") == False # Checks for number placement
    # assert is_valid("OUTATIME") == False


def test_decimals():
    assert is_valid("PI3.14") == False # Checks for alphanumeric characters
    assert is_valid("50") == False



