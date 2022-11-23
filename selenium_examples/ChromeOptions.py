import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()

prefs = {'profile.default_content_setting_values.notifications': 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                          options=chrome_options)

driver.get('https://www.way2automation.com/')
driver.maximize_window()

print(driver.title)
driver.implicitly_wait(10)
