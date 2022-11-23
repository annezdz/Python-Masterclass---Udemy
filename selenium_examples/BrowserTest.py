from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
'''
Pesquisar por https://pypi.org/project/webdriver-manager/
'''

# driver = webdriver.Chrome(executable_path="C:\\Users\\anne.zimmermann\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())


# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'C:\\Users\\anne.zimmermann\\Downloads\\geckodriver-v0.32.0-win32\\geckodriver.exe', options=options)
driver.get('http://www.way2automation.com')
driver.maximize_window()

title = driver.title
print(title)

driver.quit()

assert 'Selenium' in title