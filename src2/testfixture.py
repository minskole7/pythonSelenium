from selenium import webdriver
import pytest

# @pytest.fixture(scope="class")
# def init_chrome(request):
#     driver = webdriver.Chrome()
#     request.cls.driver = driver
#     yield
#     driver.close()


@pytest.fixture(scope="class")
def init_ff(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.close()


# @pytest.mark.usefixtures('init_chrome')
# class BaseTest:
#     pass

@pytest.mark.usefixtures('init_ff')
class BaseTestFF:
    pass


# class TestGoogle(BaseTest):
#     def test_getTiltle(self):
#         self.driver.get("https://www.google.com")
#         assert self.driver.title == "Google"


class TestFF(BaseTestFF):
    def test_getTiltle(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"

