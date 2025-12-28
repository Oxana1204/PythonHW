import allure
from selenium.webdriver.common.by import By


class LoginPage:
    """
    Данный класс представляет страницу авторизации и включает
    методы для ввода имени пользователя, пароля и нажатия кнопки входа
    """
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver

    # Локаторы элементов
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    @allure.step("Вводим значение имени пользователя в соответствующее поле формы")
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    @allure.step("Вводим пароль в соответствующее поле формы")
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажимаем кнопку входа на странице авторизации")
    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:
    """
    Представляет главную страницу каталога товаров сайта.
    Включает методы для добавления товаров в корзину и перехода в корзину
    """
    def __init__(self, driver):
        """
        Конструктор класса InventorPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver

    # Локаторы элементов
    ADD_TO_CART_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_TO_CART_BOLT_TSHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_TO_CART_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')

    @allure.step("Добавляем в корзину товар Backpack")
    def add_to_cart_backpack(self):
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    @allure.step("Добавляем в корзину товар Bolt T-Shirt")
    def add_to_cart_bolt_tshirt(self):
        self.driver.find_element(*self.ADD_TO_CART_BOLT_TSHIRT).click()

    @allure.step("Добавляем в корзину товар Onesie")
    def add_to_cart_onesie(self):
        self.driver.find_element(*self.ADD_TO_CART_ONESIE).click()

    @allure.step("Переходим в корзину покупок")
    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()


class CartPage:
    """
    Класс используется для представления страницы корзины заказа.
    Содержит метод для начала оформления покупки ("Checkout")
    """
    def __init__(self, driver):
        """
        Конструктор класса CartPage.
        :param driver: WebDriver - объект драйвера Selenium
                """
        self.driver = driver

    # Локаторы элементов
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    @allure.step("Запуск процесса оформления заказа")
    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckOutStepOnePage:
    """
    Представляет первую стадию оформления заказа,
     включая заполнение полей с информацией о покупателе
    (ФИО, почтовый индекс)
    """
    def __init__(self, driver):
        """
        Конструктор класса CheckOutStepOnePage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver

    # Локаторы элементов
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    @allure.step("Вводим имя покупателя")
    def fill_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step("Вводим фамилию покупателя")
    def fill_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Вводим почтовым кодом покупателя")
    def fill_postal_code(self, postal_code):
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys (postal_code)

    @allure.step("Продолжаем оформление заказа, нажимая кнопку продолжения")
    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()


class CheckOutCompletePage:
    """
    Класс представляет последнюю стадию оформления заказа,
    показывая итоговую сумму оплаты
    """
    def __init__(self, driver):
        """
        Конструктор класса CheckOutCompletePage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver

    # Локаторы элементов
    TOTAL_PRICE_LABEL = (By.CLASS_NAME, 'summary_total_label')

    @allure.step("Возвращает общую стоимость заказа")
    def get_total_price(self):
        total_text = self.driver.find_element(*self.TOTAL_PRICE_LABEL).text
        return float(total_text.split('$')[-1])
