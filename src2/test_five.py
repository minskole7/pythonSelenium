from selenium import webdriver
import pytest

driver = None
def setup_module(module):
    global  driver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_verifyTitle():
    assert driver.title == "Google"

def test_getCurrentUrl():
    assert "google" in driver.current_url


