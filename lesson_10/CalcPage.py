import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalcPage:
    def __init__(self, driver):
        """
        Конструктор класса CalcPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
    @allure.step("Открытие страницы калькулятора")
    def open_page(self, url):
        """
        Открываем страницу калькулятора
        """
        self.driver.get(url)
    @allure.step("Установка задержки {delay_value} секунд")
    def enter_delay_value(self, delay_value):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param delay_value: int - время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)
    @allure.step("Нажатие кнопки '{button_text}'")
    def click_button(self, button_text):
        """
        Нажимает на кнопку калькулятора.
        :param button_text: str - текст на кнопке, которую нужно нажать.
        """
        button_locator = f"//span[contains(@class, 'btn-outline-primary') and text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    @allure.step("Нажатие кнопки '{operator}'")
    def click_operator_button(self, operator):
        """
        Нажимает на кнопку калькулятора "+".
        """
        operator_locator = f"//span[contains(@class, 'operator') and text()='{operator}']"
        operator_button = self.driver.find_element(By.XPATH, operator_locator)
        operator_button.click()

    @allure.step("Нажатие кнопки '='")
    def click_equals_button(self):
        """
        Нажимает на кнопку калькулятора "=".
        """
        equals_locator = "//span[contains(@class, 'btn-outline-warning') and text()='=']"
        equals_button = self.driver.find_element(By.XPATH, equals_locator)
        equals_button.click()
    @allure.step("Получение результата с экрана калькулятора")
    def get_result_text(self):
        """
        Возращает текущий результат с экрана калькулятора.
        :return: str - текст резальтата на экране калькулятора.
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
