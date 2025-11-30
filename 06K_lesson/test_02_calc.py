from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)  # 45 секунд + запас

    try:
        # Шаг 1: Открыть страницу
        print("Открываю страницу калькулятора")
        driver.get(
            "http://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()

        # Шаг 2: Ввести значение 45 в поле delay
        print("Устанавливаю задержку 45 секунд")
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Шаг 3: Нажать кнопки 7 + 8 =
        print("Выполняю вычисление: 7 + 8")

        # Кнопка 7
        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

        # Кнопка +
        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

        # Кнопка 8
        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()

        # Кнопка =
        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()

        # Шаг 4: Проверить результат через 45 секунд
        print("Ожидаю результат 15 через 45 секунд")

        # Ждем пока результат станет равным 15
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # Получаем фактический результат для проверки
        actual_result = driver.find_element(By.CLASS_NAME, "screen").text

        # Проверяем assert'ом
        assert actual_result == "15", \
            f"Ожидался результат 15, но получили {actual_result}"

        print("Результат 15 отобразился корректно!")
        print(f"Фактический результат: {actual_result}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        driver.save_screenshot("calc_error.png")
        raise

    finally:
        driver.save_screenshot("calc_result.png")
        driver.quit()
        print("Браузер закрыт.")


if __name__ == "__main__":
    test_slow_calculator()
