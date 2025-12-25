from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = (webdriver.Chrome
          (service=ChromeService(ChromeDriverManager().install())))
driver.implicitly_wait(10)

driver.get('http://uitestingplayground.com/textinput')
field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

wait = WebDriverWait(driver, 20)
content = wait.until(EC.visibility_of_element_located
                     ((By.CSS_SELECTOR, "#updatingButton")))
txt = content.text
print(txt)

driver.quit()
