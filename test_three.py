import pytest
@pytest.mark.login
def test_wordone_login():
    number = 100
    assert  number > 100

@pytest.mark.logout
def test_wordone_logout():
    number = 100
    assert number >= 100
