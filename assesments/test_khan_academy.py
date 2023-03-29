import datetime
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            # "appPackage": "org.khanacademy.android",
            # "appActivity": "org.khanacademy.android.ui.library.MainActivity",
            # "noReset": True
            # "udid":"emulator-5554"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestNotification(AppiumConfig):
    def test_notification(self):
        if self.driver.is_app_installed("org.khanacademy.android"):
            self.driver.remove_app("org.khanacademy.android")

        self.driver.install_app(r"C:\PythonTraining15Feb\Components\khan-academy-7-3-2.apk")
        self.driver.activate_app("org.khanacademy.android")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Allow']").click()

        if len(self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")')) == 1:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Search tab']").click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Math"]').click()

        while len(self.driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@text='Class 12 math (India)']")) == 0:
            self.driver.swipe(500, 1700, 500, 700, 600)

        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Class 12 math (India)']").click()


        while len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Take Course Challenge']")) == 0:
            self.driver.swipe(500, 1700, 500, 700, 600)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Take Course Challenge']").click()
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button)[2]').click()
