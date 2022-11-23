import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://www.way2automation.com')
driver.maximize_window()
driver.implicitly_wait(10)

windows = driver.window_handles

for window in windows:
    print(window)

driver.find_element(By.XPATH, "//li[@id='menu-item-27625']//span["
                              "@class='menu-text'][normalize-space()='Member "
                              "Login']")


# windows = driver.window_handles
#
# for window in windows:
#     print(window)
#     driver.switch_to.window(window)

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, "//input[@id='email']")\
    .send_keys('trainer@way2automation.com')

driver.close()