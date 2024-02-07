import pytest

def test_one():
    number = 100
    assert  number > 100

@pytest.mark.login
def test_two():
    print("login testcase one")
    number = 100
    assert number >= 100