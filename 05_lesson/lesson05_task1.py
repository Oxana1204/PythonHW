from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/classattr")
blue_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()
browser.quit()

sleep(15)
