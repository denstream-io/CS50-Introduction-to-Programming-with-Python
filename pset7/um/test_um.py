from um import count

def main():
    test_substring()
    test_case_sensitivity()
    test_special_characters()


def test_substring():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("yummy") == 0

def test_case_sensitivity():
    assert count("Um") == 1
    assert count("Um Um") == 2
    assert count("yUmmy") == 0

def test_special_characters():
    assert count("um?") == 1
    assert count("um!") == 1