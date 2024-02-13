from selenium import webdriver
import pytest
driver = None
@pytest.fixture(params=["chrome","chrome2"],scope='class')
def init_driver(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
    elif request.param == "chrome2":
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
    else:
        print("incorrect driver")

    yield driver
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_title(self):
        assert driver.title == "Google"
    def test_google_title(self):
        assert "google" in driver.current_url





















