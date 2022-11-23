import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get')
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame('iframeResult')
driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()

# voltando para a janela principal

# driver.switch_to.default_content() ou
driver.switch_to.window(driver.window_handles[0])

# achar iframes

frames = driver.find_elements(By.TAG_NAME, 'iframe')

for frame in frames:
    print(frame.get_attribute('id'))

print(len(frames))
time.sleep(3)
