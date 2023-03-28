import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
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

class TestAdvanceCode(AppiumConfig):
    def test_tap_using_coordinates(self):
        if len(self.driver.find_elements(AppiumBy.ID, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        action = TouchAction(self.driver)
        action.tap(x=900,y=1200,count=5).perform()
        time.sleep(5)

    def test_tap_using_coordinates(self):
        if len(self.driver.find_elements(AppiumBy.ID, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        action = TouchAction(self.driver)
        action.tap(self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Arts and humanities']"), count=5).perform()

    def test_long_press_webelement(self):
        time.sleep(10)
        self.driver.press_keycode(AndroidKey.HOME)
        time.sleep(2)
        self.driver.swipe(902,1174,902,100)
        action = TouchAction(self.driver)
        action.long_press(self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Khan')]"),duration=100).perform()
        self.driver.find_element(AppiumBy.XPATH,"//*[contains(@text,'App in')]").click()

    def test_press(self):
        action = TouchAction(self.driver)
        action.press(100, 100).wait(1000).move_to(200, 200).release()



