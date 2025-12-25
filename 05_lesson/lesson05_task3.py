from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
browse = webdriver.Firefox(options=options)
browse.get("http://the-internet.herokuapp.com/inputs")
search_field = browse.find_element(By.CSS_SELECTOR, "input")
search_field.send_keys("Sky")

sleep(5)

search_field.clear()
search_field.send_keys("Pro")
browse.quit()
