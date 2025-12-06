from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    ADD_TO_CART_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_TO_CART_BOLT_TSHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_TO_CART_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')

    def add_to_cart_backpack(self):
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    def add_to_cart_bolt_tshirt(self):
        self.driver.find_element(*self.ADD_TO_CART_BOLT_TSHIRT).click()

    def add_to_cart_onesie(self):
        self.driver.find_element(*self.ADD_TO_CART_ONESIE).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckOutStepOnePage:
    def __init__(self, driver):
        self.driver = driver

    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_postal_code(self, postal_code):
        (self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys /
         (postal_code))

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()


class CheckOutCompletePage:
    def __init__(self, driver):
        self.driver = driver

    TOTAL_PRICE_LABEL = (By.CLASS_NAME, 'summary_total_label')

    def get_total_price(self):
        total_text = self.driver.find_element(*self.TOTAL_PRICE_LABEL).text
        return float(total_text.split('$')[-1])
