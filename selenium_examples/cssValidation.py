import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://www.w3schools.com/css/default.asp')
driver.maximize_window()

print(driver.find_element(By.XPATH, "//a[normalize-space()='CSS Box Model']")
      .value_of_css_property('font-size'))

print(driver.find_element(By.XPATH, "//a[normalize-space()='CSS Box Model']")
      .value_of_css_property('font-family'))

print(driver.find_element(By.XPATH, "//a[normalize-space()='CSS Box Model']")
      .value_of_css_property('color'))



