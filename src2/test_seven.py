from selenium import webdriver
import pytest
driver = None
@pytest.fixture(params=["chrome","ff"],scope='class')
def init_driver(request):
    driver = None
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
    elif request.param == "ff":
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")
    else:
        print("incorrect driver")
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_title(self):
        assert self.driver.title == "Google"






















