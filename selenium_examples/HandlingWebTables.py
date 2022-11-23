import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://www.espncricinfo.com/series/a20-league-2020-21-1255254'
           '/points-table-standings')
driver.maximize_window()
driver.implicitly_wait(10)

rows = driver.find_elements(By.XPATH, '//tbody/tr')

cols = driver.find_elements(By.XPATH, '//tbody/tr[1]/td')
total_rows = len(rows)

total_cols = len(cols)

print('Total rows are : ', total_rows, ' and total cols are: ', total_cols)

for row in rows:
    print(row.text)

print('Second Way')

start_path = "//tbody/tr["
mid_xpath = "]/td["
end_xpath = "]"
teste_xpath = "//tbody/tr["
end_test = "]/td["
end = "]"

for row in range(1, 2):
    for col in range(1, 12):
        print(driver.find_element(By.XPATH,
                                  teste_xpath + str(row) + end_test
                                  + str(col) + end).text)
