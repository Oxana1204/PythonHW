import pytest
from selenium import webdriver
from ShopPage import LoginPage, InventoryPage, CartPage, CheckOutStepOnePage, CheckOutCompletePage
import allure


@pytest.fixture(scope="module")
def browser():
    with allure.step("Инициализация браузера"):
        driver = webdriver.Firefox()
        yield driver
        driver.quit()


@allure.feature("Процесс покупки товаров")
@allure.story("Проверка полного цикла покупок на сайте SauceDemo")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тестирование процесса покупки трех товаров")
@allure.description("Этот тест проверяет полный цикл /"
                    "покупки трех товаров начиная с авторизации")
def test_shopping_flow(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    check_out_step_one_page = CheckOutStepOnePage(browser)
    check_out_complete_page = CheckOutCompletePage(browser)

    with allure.step("Открытие главной страницы сайта"):
         browser.get("https://www.saucedemo.com/")

    with allure.step("Авторизация стандартного пользователя"):
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_login_button()

    with allure.step("Добавление трех товаров в корзину"):
        inventory_page.add_to_cart_backpack()
        inventory_page.add_to_cart_bolt_tshirt()
        inventory_page.add_to_cart_onesie()

    with allure.step("Переход в корзину"):
         inventory_page.go_to_cart()

    with allure.step("Нажатие кнопки Checkout"):
         cart_page.checkout()

    with allure.step("Заполнение формы оформления заказа"):
        check_out_step_one_page.fill_first_name('Оксана')
        check_out_step_one_page.fill_last_name('Сазонова')
        check_out_step_one_page.fill_postal_code('160014')
        check_out_step_one_page.continue_checkout()

    with allure.step("Проверка итоговой цены заказа"):
        total_price = check_out_complete_page.get_total_price()
        expected_price = 58.29
        assert float(total_price) == expected_price

