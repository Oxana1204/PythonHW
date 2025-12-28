import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """
       Представляет страницу формы ввода данных, используемую для тестирования веб-интерфейсов.
       Этот класс предназначен для автоматизации заполнения и отправки форм на сайте.
       Использует библиотеку Selenium для взаимодействия с элементами страницы.

       Attributes:
           driver (WebDriver): Объект драйвера Selenium, переданный при создании экземпляра класса.
           wait (WebDriverWait): Объект ожидания элементов страницы.
           fields (dict): Словарь полей формы и соответствующих им тестовых значений.

       Methods:
           open(): Открывает страницу формы.
           fill_form(): Заполняет форму значениями из атрибута fields.
           submit_form(): Отправляет заполненную форму.
           get_field_class(field_id): Получает значение атрибута class элемента по ID.
           check_zip_code_error(): Проверяет наличие ошибки в поле zip-code.
           check_fields_success(): Проверяет успешность заполнения всех обязательных полей.
           check_form_submission(): Проведение итогового теста правильности заполнения формы.
       """
    def __init__(self, driver):
        """
        Конструктор класса FormPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        # Значения по умолчанию для каждого поля формы
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "", # Оставляем пустое значение для проверки ошибки
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }
    @allure.step("Открывает целевую страницу формы")
    def open(self):
        """
        Открывает целевую страницу формы.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    @allure.step("Заполняет форму введенными значениями из атрибута fields")
    def fill_form(self):
        """
        Заполняет форму введенными значениями из атрибута fields.
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)
    @allure.step("Отправляет заполненную форму нажатием кнопки Submit")
    def submit_form(self):
        """
        Отправляет заполненную форму нажатием кнопки Submit.
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()
    @allure.step("Получает значение атрибута class HTML-элемента по его id")
    def get_field_class(self, field_id):
        """
        Получает значение атрибута class HTML-элемента по его id.

        :param str field_id: Идентификатор HTML-элемента.
        :return: Атрибут class указанного элемента.
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element
    @allure.step("Проверяет наличие ошибки в поле ZIP-кода")
    def check_zip_code_error(self):
        """
        Проверяет наличие ошибки в поле ZIP-кода.

        :return bool: True, если ошибка присутствует (класс alert-danger); иначе False.
        """
        return "alert-danger" in self.get_field_class("zip-code")
    @allure.step("Проверяет правильность заполнения обязательных полей формы")
    def check_fields_success(self):
        """
        Проверяет правильность заполнения обязательных полей формы.

        :return bool: True, если все обязательные поля успешно заполнены; иначе False.
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True
    @allure.step("Итоговая проверка результатов заполнения и отправки формы")
    def check_form_submission(self):
        """
        Итоговая проверка результатов заполнения и отправки формы.
        Утверждения проверяют корректность обработки ошибок и успешного заполнения остальных полей.
        """
        assert self.check_zip_code_error(), "поле Zip code подсвечено красным"
        assert self.check_fields_success(), "остальные поля подсвечены зеленым"
