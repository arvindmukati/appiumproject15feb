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
                # "udid": "7DDEEEJ7UCGYINMR",
                "deviceName": "realme",
                "appPackage": "org.khanacademy.android",
                "appActivity": "org.khanacademy.android.ui.library.MainActivity",
                "noReset": "true"
            }
            self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                           desired_capabilities=desc_cap)
            self.driver.implicitly_wait(15)
            yield
            self.driver.quit()


class TestAndroidDeviceLocal(AppiumConfig):
    def test_invalid_login(self):
        # presence of element - using length
        # if len(self.driver.find_elements(AppiumBy.ID, "//android.widget.TextView[@text='Dismiss']")) > 0:
        #     self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH,
                                 "//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys(
            "dina")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc,'Pass')]").send_keys(
            "dina123")
        # click on sign in
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
        # get the text "There was an issue signing in" and print it
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
        print(actual_error)