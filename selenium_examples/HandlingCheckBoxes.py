import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('http://www.tizag.com/htmlT/htmlcheckboxes.php')
driver.maximize_window()
driver.implicitly_wait(10)

# driver.find_element(By.XPATH, '//div[4]//input[1]').click()
# driver.find_element(By.XPATH, '//div[4]//input[2]').click()
# driver.find_element(By.XPATH, '//div[4]//input[3]').click()
# driver.find_element(By.XPATH, '//div[4]//input[4]').click()

# i = 1
#
# while is_element_present(By.XPATH, "//div[4]/input["+str(i)+"]"):
#     driver.find_element(By.XPATH, "//div[4]/input["+str(i)+"]").click()
#     i += 1

# print('Total checkboxes are :', i - 1)

checkboxes = driver.find_elements(By.NAME, 'sports')
print(len(checkboxes))

block = driver.find_element(By.XPATH, "//div[@class='display'][1]")

checkbox_in_block = block.find_elements(By.NAME, 'sports')
print(len(checkbox_in_block))

for checkbox in checkboxes:
    print('Before clicking: ', checkbox.is_selected())
    checkbox.click()
    print('After clicking: ', checkbox.is_selected())

time.sleep(3)
