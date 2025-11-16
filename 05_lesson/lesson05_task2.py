from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(" http://uitestingplayground.com/dynamicid")
blue_button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
blue_button.click()
browser.quit()

sleep(15)
