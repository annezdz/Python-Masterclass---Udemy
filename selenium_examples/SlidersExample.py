import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://jqueryui.com/resources/demos/slider/default.html')
driver.maximize_window()
driver.implicitly_wait(10)

mainSlider = driver.find_element(By.ID, 'slider')

location = mainSlider.location
size = mainSlider.size
print(location)

w, h = size['width'], size['height']

print(w, h)

slider = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle "
                                       "ui-corner-all ui-state-default']")
#
# ActionChains(driver).drag_and_drop_by_offset(slider, 400, 0).perform()

ActionChains(driver).drag_and_drop_by_offset(slider, w / 2, 0).perform()

time.sleep(3)
