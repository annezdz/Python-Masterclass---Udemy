import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://deluxe-menu.com/popup-mode-sample.html')
driver.maximize_window()
driver.implicitly_wait(10)

img = driver.find_element(By.XPATH, "//img[@src='data-samples/images"
                                    "/popup_pic.gif']")
#
# alert = Alert(driver)
#
# print(alert.text)
# time.sleep(3)
# alert.accept()

alert = driver.switch_to.alert

print(alert.text)
time.sleep(3)
alert.accept()