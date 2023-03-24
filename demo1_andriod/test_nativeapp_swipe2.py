import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


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
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=desc_cap)
        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()


class TestAndroidDevice(AppiumConfig):

    def test_scroll_to_himalaya(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

            # id is resource-id only
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        # ACCESSIBILITY_ID is content-desc in android
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Search tab").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        time.sleep(5)
        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.XPATH,"//*[@text ='Art of Asia']")) == 0:
            self.driver.swipe(902, 1174, 902, 794, 1000)

        self.driver.find_element(AppiumBy.XPATH,"//*[@text ='Art of Asia']").click()
        self.driver.implicitly_wait(30)
        time.sleep(5)
