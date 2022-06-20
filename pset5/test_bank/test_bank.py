from bank import value

def test_spaces():
    assert value("Hello") == 0
def test_name():
    assert value("Hello, Newman") == 0

def test_question():
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100
    assert value("What's up?") == 100
