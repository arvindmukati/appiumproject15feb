import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig():
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        desc_cap = {
            "platformName": "android",
            "udid": "7DDEEEJ7UCGYINMR",
            "deviceName": "realme",
            "appPackage": "org.khanacademy.android",
            "appActivity": "org.khanacademy.android.ui.library.MainActivity"
        }
        # "app": r"C:\PythonTraining15Feb\Components\khan-academy-7-3-2.apk",
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=desc_cap)
        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()


class TestAndroidDevice(AppiumConfig):
    def test_invalid_login_in(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().descriptionContains("e-mail address")').send_keys("Dina123")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().descriptionContains("Pass")').send_keys(
            "Password")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().text("Sign in").instance(1)').click()
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().textContains("issu")').text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("issu")').get_attribute("text")
        print(actual_error)
