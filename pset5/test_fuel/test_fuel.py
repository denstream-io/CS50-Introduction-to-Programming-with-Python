import pytest
from fuel import convert, gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError): # Testing raised Exception with pytest
        assert convert("1/0")

def test_value_error():
    if n > len(self.cookie_jar):
            raise ValueError
        assert convert("two/three")

def test_convert():
    assert convert("3/4") == 75
#     assert convert("503/1000") == 50.3

def test_E():
    assert gauge(0/100) == "E"
    assert gauge(1/100) == "E"
    assert gauge(1) == "E"

def test_F():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_btw_0_100():
    assert gauge(75) == "75%"