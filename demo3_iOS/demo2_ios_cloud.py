import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
            # Specify device and os_version for testing
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": "arvindmukati_JrVmNs",
                "accessKey": "UkTXPLoCvroZZSqBTttb",
                "projectName": "Third Python project",
                "buildName": "browserstack-build-1-ios",
                "sessionName": "BStack first_test-ios"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestSampleApp(AppiumIosConfig):
    def test_text_box(self):
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Text']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@name='Text Input' and @value='Enter a text']").send_keys("hello")

        # self.driver.back()
        self.driver.find_element(AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='UI Elements'])[1]").click()

        # click on alert
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Alert Button']").click()
        # get the text and assert - This is a native alert
        text =self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='This is a native alert.']").text
        assert_that("This is a native alert.").is_equal_to(text)
        # click on ok
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='OK']").click()
        time.sleep(5)

