import pytest
from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12 # calls the getter method

def test_str():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(4)
# To be continued