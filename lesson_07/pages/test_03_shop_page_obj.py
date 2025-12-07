import pytest
from selenium import webdriver
from lesson_07.pages.ShopPage import LoginPage, InventoryPage, CartPage, CheckOutStepOnePage, CheckOutCompletePage


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shopping_flow(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    check_out_step_one_page = CheckOutStepOnePage(browser)
    check_out_complete_page = CheckOutCompletePage(browser)

    # Открываем главную страницу сайта
    browser.get("https://www.saucedemo.com/")

    # Авторизуемся стандартным пользователем
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()

    # Добавляем три товара в корзину
    inventory_page.add_to_cart_backpack()
    inventory_page.add_to_cart_bolt_tshirt()
    inventory_page.add_to_cart_onesie()

    # Переходим в корзину
    inventory_page.go_to_cart()

    # Нажимаем кнопку Checkout
    cart_page.checkout()

    # Заполняем форму оформления заказа
    check_out_step_one_page.fill_first_name('Оксана')
    check_out_step_one_page.fill_last_name('Сазонова')
    check_out_step_one_page.fill_postal_code('160014')
    check_out_step_one_page.continue_checkout()

    # Проверяем итоговую цену заказа
    total_price = check_out_complete_page.get_total_price()
    assert total_price == 58.29, f'Итоговая цена должна быть $58.29, но была {total_price}'
