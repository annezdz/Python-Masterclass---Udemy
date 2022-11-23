import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

firefox_options = Options()

firefox_options.set_preference('dom.webnotifications.enabled', False)
firefox_options.headless = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                           options=firefox_options)

driver.get('https://www.redbus.com/')
driver.maximize_window()

print(driver.title)
driver.implicitly_wait(10)
