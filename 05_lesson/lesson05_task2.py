from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/dynamicid")
blue_button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
blue_button.click()

sleep(15)

browser.quit()
