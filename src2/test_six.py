from selenium import webdriver
import pytest
driver = None
@pytest.fixture(scope = 'module')
def init_launch():
    global  driver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    yield


@pytest.mark.usefixtures('init_launch')
def test_verifyTitle():
    assert driver.title == "Google"

@pytest.mark.usefixtures('init_launch')
def test_getCurrentUrl():
    assert "google" in driver.current_url


def test_getCurrentUrl2():
    assert "https" in driver.current_url



