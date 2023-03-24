import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey


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

        size_dic = self.driver.get_window_size()
        print(size_dic)
        x1 = size_dic["width"]*(50/100)
        y1 = size_dic["height"] * (75 / 100)
        x2 = size_dic["width"] * (50 / 100)
        y2 = size_dic["height"] * (25 / 100)
        print(x1)
        print(y1)
        print(x2)
        print(y2)

        time.sleep(5)
        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text ='Art of Asia']")) == 0:
            self.driver.swipe(x1, y1, x2, x2, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Asia')]").click()
        self.driver.implicitly_wait(30)
        self.driver.press_keycode(AndroidKey.BACK)
        time.sleep(5)