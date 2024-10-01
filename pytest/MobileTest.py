from lib2to3.pgen2 import driver
import pytest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time


@pytest.fixture(scope="class")
def mobile_driver_init(request):
    global driver
    caps = {
        "platformName": "Android",
        "uiautomationName": "UiAutomator2",
        "deviceName": "RR8T30384JP",
        "appPackage": "io.selendroid.testapp",
        "appActivity": "io.selendroid.testapp.HomeScreenActivity"
    }

    url = "http://127.0.0.1:4723/wd/hub"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps))
    driver.implicitly_wait(5)


def teardown_function(function):
    driver.quit()


def test_testing_function(mobile_driver_init):
    el1 = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/continue_button")
    el1.click()


def test_verify(mobile_driver_init):
    button = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/continue_button")
    if button.is_displayed():
        print("Passed")
    else:
        print("Not Passed")