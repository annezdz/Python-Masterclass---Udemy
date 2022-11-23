from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://google.com')
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@title='Search']")))
# element = driver.find_by_xpath("//input[@title='Search']")
# time.sleep(3)
# element.send_keys("annezdz@hotmail.com")
driver.implicitly_wait(20)
# driver.find_element_by_id("identifierId").send_keys("annezdz@hotmail.com")
