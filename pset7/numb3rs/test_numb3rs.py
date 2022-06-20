from numb3rs import validate

def main():
    test_format()
    test_range()
    test_length()
    test_string()




def test_format():
    assert validate('127.0.0.1') == True
    assert validate('127:0:0:1') == False
    assert validate('127.0.0') == False
    assert validate('127.0') == False
    assert validate('127') == False
def test_range():
    assert validate('255.255.255.255') == True
    assert validate('256.255.255.255') == False
    assert validate('255.256.255.255') == False
    assert validate('255.255.256.255') == False
    assert validate('255.255.255.256') == False

def test_length():
    assert validate('0.0.0.0') == True
    assert validate('0.0.0.0.0') == False

def test_string():
    assert validate("cat") == False
    assert validate("dog") == False




