import pytest

def test_six():
    first_name = "chinmay"
    assert  first_name  == "chinmay"

@pytest.mark.login
def test_seven():
    print("login test case four")
    first_name = "chinmay"
    assert  first_name  == "chinmay"