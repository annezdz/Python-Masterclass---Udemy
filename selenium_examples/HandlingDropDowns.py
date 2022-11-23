import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver.get('https://echoecho.com/htmlforms11.htm')
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# driver.find_element(By.XPATH, "//select[@name='dropdownmenu']").send_keys('Cheese')
# driver.find_element(By.NAME, "dropdownmenu").send_keys('Cheese')
driver.get('https://www.wikipedia.org/')
dropdown = driver.find_element(By.ID, 'searchLanguage')
select = Select(dropdown)

# selecionando por texto visível
# select.select_by_visible_text('Eesti')

# selecionando por valor
select.select_by_value('ar')

# imprimindo todos os aíses e linguas
options = driver.find_elements(By.TAG_NAME, 'option')

for option in options:
    print('Texts is: ', option.text, ' Language is: ',
          option.get_attribute('lang'))

print('Total dropdowns elements are ', len(options))
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, 'a')

for link in links:
    print('Link text - ', link.text, '--- URL : ', link.get_attribute('href'))
print('Total links = ', len(links))

print('------------ footer ---------------')

block = driver.find_elements(By.XPATH, "//*[@class='footer']/div/div")

print('1 link is : ', block.__getitem__(0).text)
