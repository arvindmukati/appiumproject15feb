import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

class AppiumConfig():
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        desc_cap = {
            "platformName": "android",
            "deviceName": "realme",
            "app": r"C:\PythonTraining15Feb\Components\com.bsl.hyundai_2021-08-09.apk",
            "udid": "7DDEEEJ7UCGYINMR"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=desc_cap)
        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()

class TestAndroidDevice(AppiumConfig):

    def test_def(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='DENY']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='DENY']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SIGN UP!']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Name*']").send_keys("peter")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email ID*']").send_keys("peter@123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile Number*']").send_keys("9778")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password*']").send_keys("pass")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password*']").send_keys("Hello")
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.bsl.hyundai:id/checkAcceptTermsCondition']").click()
        time.sleep(5)


