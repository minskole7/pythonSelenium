import  pytest
@pytest.mark.login
def test_wordtwo_login():
    number = 100
    assert  number > 100

@pytest.mark.logout
def test_wordtwo_logout():
    number = 100
    assert number >= 100

