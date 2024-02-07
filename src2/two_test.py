import  pytest

@pytest.mark.login
def test_three():
    print("login test case two")
    first_name = "chinmay"
    assert  first_name  == "chinmay"

def test_four():
    canDrive = True
    assert canDrive == True