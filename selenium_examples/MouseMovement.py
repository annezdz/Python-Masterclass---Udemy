import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('http://www.way2automation.com')
driver.maximize_window()
driver.implicitly_wait(10)


menu = driver.find_element(By.XPATH, "//li[@id='menu-item-27617']//span["
                              "@class='menu-text'][normalize-space("
                              ")='Resources']")

action = ActionChains(driver)
action.move_to_element(menu).perform()

driver.find_element(By.XPATH, "//li[@id='menu-item-27619']//span["
                              "@class='menu-text'][normalize-space("
                              ")='Practice Site 2']").click()