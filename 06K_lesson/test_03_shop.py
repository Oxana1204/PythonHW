from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_sauce_demo_store():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 5)

    try:
        # Шаг 1: Открыть сайт магазина в Firefox
        print("Открываю сайт магазина")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Шаг 2: Авторизация как standard_user
        print("Авторизуюсь как standard_user")
        username_input = wait.until \
            (EC.element_to_be_clickable((By.ID, "user-name")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Ждем пока загрузится список товаров
        print("Жду загрузки страницы продуктов")
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

        wait = WebDriverWait(driver, 10)

        # Шаг 3: Добавить товары в корзину
        print("Добавляю товары в корзину")

        # Sauce Labs Backpack
        backpack_button = wait.until(EC.element_to_be_clickable \
                        ((By.ID,  "add-to-cart-sauce-labs-backpack")))
        backpack_button.click()

        print("Sauce Labs Backpack добавлен")

        # Ждем пока кнопка сменится на "Remove"
        wait.until(EC.text_to_be_present_in_element \
                       ((By.ID, "remove-sauce-labs-backpack"), "Remove"))

        # Sauce Labs Bolt T-Shirt
        tshirt_button = wait.until \
            (EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        tshirt_button.click()
        print("Sauce Labs Bolt T-Shirt добавлен")

        #Ждем пока кнопка сменится на "Remove"
        wait.until(EC.text_to_be_present_in_element((By.ID, "remove-sauce-labs-bolt-t-shirt"), "Remove"))

        # Sauce Labs Onesie
        onesie_button = wait.until \
            (EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        onesie_button.click()
        print("Sauce Labs Onesie добавлен")

        # Ждем пока кнопка сменится на "Remove"
        wait.until(EC.text_to_be_present_in_element \
                       ((By.ID, "remove-sauce-labs-onesie"), "Remove"))

        # Шаг 4: Перейти в корзину
        print("Перехожу в корзину")
        cart_icon = wait.until \
            (EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()

        # Ждем пока загрузится страница корзины
        print("Жду загрузки корзины")
        wait.until(EC.visibility_of_element_located \
                       ((By.CLASS_NAME, "cart_item")))

        # Шаг 5: Нажать Checkout
        print("Нажимаю Checkout")
        checkout_button = wait.until \
            (EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Шаг 6: Заполнить форму данными
        print("Заполняю форму данными")

        #Ждем пока загрузится форма
        wait.until(
            EC.presence_of_element_located((By.ID,"first-name")))

        first_name = driver.find_element(By.ID, "first-name")
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")

        first_name.send_keys("Оксана")
        last_name.send_keys("Сазонова")
        postal_code.send_keys("160014")

        continue_button.click()

        # Шаг 7: Прочитать итоговую стоимость
        print("Читаю итоговую стоимость")

        #Ждем пока загрузится итоговая страница
        print("Жду загрузки итоговой страницы")
        total_element = wait.until \
            (EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))

        total_text = total_element.text
        total_value = total_text.replace("Total: $", "")

        print(f"Итоговая стоимость: {total_text}")

        # Шаг 8: Проверить, что сумма равна $58.29
        expected_total = "58.29"
        assert total_value == expected_total, \
            f"Ожидалась сумма ${expected_total}, но получили ${total_value}"

        print("Тест пройден успешно!")
        print(f"Итоговая сумма корректна: ${total_value}")
        driver.save_screenshot("store_8.png")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        driver.save_screenshot("store_error.png")
        raise

    finally:
        # Шаг 9: Закрыть браузер
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_sauce_demo_store()
