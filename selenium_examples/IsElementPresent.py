from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium_examples.HandlingCheckBoxes import is_element_present

# def is_element_present(how, what):
#     try:
#         driver.find_element(by=how, value=what)
#         return True
#     except NoSuchElementException:
#         return False

# def is_element_present(how, what):
#     if len(driver.find_elements(by=how, value=what)) == 0:
#         return False
#     else:
#         return True


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://gmail.com')
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.find_element(By.ID, 'identifierId').is_displayed())  # True

# print(is_element_present('identifierId'))
print(is_element_present(By.ID, 'identifierId'))
