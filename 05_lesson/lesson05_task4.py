from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.XPATH, ' //input[@id="username"] ')
username_input.send_keys("tomsmith")

password_input = driver.find_element(By.XPATH, ' //input[@id="password"] ')
password_input.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CSS_SELECTOR,  ".fa.fa-2x.fa-sign-in")
button.click()

text = driver.find_element(By.CLASS_NAME, 'flash.success').text.strip()

print(text)

driver.quit()
