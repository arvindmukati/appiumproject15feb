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
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()

        self.driver.find_element(AppiumBy.XPATH,
                                 "//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys(
            "Dina123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys(
            "Password")
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
        print(actual_error)

    def test_sign_in(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign up with email']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='First name']").send_keys("john")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Last name']").send_keys("peter")
        # self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign up with email']").end_keys()

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").click()

        # choose Aug
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").clear()
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").send_keys("Aug")

        # choose 20
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").send_keys(
            "20")

        # choose 1995
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").send_keys(
            "1995")

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email address']").send_keys("abc123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password']").send_keys("abc")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='CREATE']").click()
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
        print(actual_error)
        assert_that(actual_error).is_equal_to("There was an issue signing in")
