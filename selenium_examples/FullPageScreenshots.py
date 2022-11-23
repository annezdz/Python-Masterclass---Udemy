import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://www.way2automation.com')
driver.maximize_window()
driver.implicitly_wait(10)

driver.save_screenshot("./screenshots/errorFullPage.jpg")

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
driver.set_window_size(S('Width'), S('Height'))

driver.find_element(By.TAG_NAME, 'body').screenshot('./screenshots/fullPage.jpg')