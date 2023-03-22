import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desc_cap = {
    "platformName": "android",
    "deviceName": "realme",
    "app": r"C:\PythonTraining15Feb\Components\khan-academy-7-3-2.apk"
}

driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=desc_cap)
driver.implicitly_wait(15)
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys("Dina123")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='Password']").send_keys("Password")

driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@text='Sign in'])[2]").click()

actual_error = driver.find_element(AppiumBy.XPATH,"//*[contains(@text,'issue')]").text
print(actual_error)
actual_error = driver.find_element(AppiumBy.XPATH,"//*[contains(@text,'issue')]").get_attribute("text")
print(actual_error)


print(driver.page_source)
time.sleep(3)
driver.quit()