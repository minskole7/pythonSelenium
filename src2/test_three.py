import pytest
def test_four():
    first_name = "chinmay"
    assert  first_name  == "chinmay"

@pytest.mark.login
def test_five():
    print("login test case 3")
    first_name = "chinmay"
    assert  first_name  == "chinmay"