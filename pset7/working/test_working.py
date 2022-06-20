from working import convert
import pytest


def test_incorrect_hours():
    with pytest.raises(ValueError):
        assert convert("13 PM to 13 AM")

def test_incorrect_minutes():
    with pytest.raises(ValueError):
        assert convert("8:60 AM to 4:60 PM")
def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_incorrect_format():
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")

