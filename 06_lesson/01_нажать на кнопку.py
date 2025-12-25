from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = (webdriver.Chrome
          (service=ChromeService(ChromeDriverManager().install())))
driver.implicitly_wait(15)

driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

wait = WebDriverWait(driver, 30)
element = wait.until(EC.visibility_of_element_located
                     ((By.CSS_SELECTOR, "p.bg-success")))

txt = element.text
print(txt)

driver.quit()
