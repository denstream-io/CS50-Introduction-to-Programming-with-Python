from seasons import get_date


def test_format():
    assert get_date("1999-01-01") == "Twelve million, three hundred thirty-two thousand, one hundred sixty minutes"
    # assert get_age("1998-01-01") == "One million, fifty-one thousand, two hundred minutes"
    # assert get_age("1995-01-01") == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    # assert get_age("1998-06-01") == "Eight hundred thirty-three thousand, seven hundred sixty minutes"
    # assert get_age("1998-06-20") == "Eight hundred six thousand, four hundred minutes"