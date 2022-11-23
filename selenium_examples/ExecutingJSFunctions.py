import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://www.w3schools.com/jsref/tryit.asp?filename'
           '=tryjsref_submit_get')
driver.maximize_window()
driver.implicitly_wait(10)


def capture_screenshot(web_driver, path):
    file_name = path + 'screenshot_' + time.asctime().replace(':', '_') + ".jpg"
    web_driver.save_screenshot(file_name)


# salvando um screenshot

driver.save_screenshot("./screenshots/error.jpg")
driver.switch_to.frame('iframeResult')
# driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()

# Exemplo usando JS functions

driver.execute_script('myFunction()')
element = driver.find_element(By.ID, 'mySubmit')
element.screenshot("./screenshots/element.jpg")
driver.execute_script("arguments[0].style.border='3px solid red'", element)

driver.switch_to.default_content()

# voltando para a janela principal

# driver.switch_to.default_content() ou
driver.switch_to.window(driver.window_handles[0])

# achar iframes

frames = driver.find_elements(By.TAG_NAME, 'iframe')

for frame in frames:
    print(frame.get_attribute('id'))

print(len(frames))

capture_screenshot(driver, "./screenshots/")
time.sleep(3)
