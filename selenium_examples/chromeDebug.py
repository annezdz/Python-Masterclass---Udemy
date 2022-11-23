import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

chrome_options.add_experimental_option('debuggerAddress', "localhost:9222")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://www.gmail.com')
driver.maximize_window()