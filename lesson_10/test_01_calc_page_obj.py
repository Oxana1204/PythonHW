from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalcPage import CalcPage
import pytest
import allure


@pytest.fixture
def driver():
    """
    Фикситура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Добавили декораторы Allure
@allure.title("Тестирование калькулятора с задержкой")
@allure.description("Проверка правильности вычисления выражения с задержкой")
@allure.feature("Функционал калькулятора")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    calculator_page = CalcPage(driver)

    # Шаг открытия страницы с декорированным названием
    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Задержка ввода значения
    with allure.step("Установка задержки расчета на 45 секунд"):
        calculator_page.enter_delay_value("45")

    # Нажатия кнопок
    with allure.step("Ввод чисел и операций"):
        calculator_page.click_button("7")  # нажимаем цифру 7
        calculator_page.click_operator_button("+")  # нажимаем плюс
        calculator_page.click_button("8")  # нажимаем цифру 8
        calculator_page.click_equals_button()  # нажимаем равно

    # Ожидание появления результата
    with allure.step("Ожидаем появление результата на экране"):
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    # Извлекаем значение экрана
    with allure.step("Получение текущего результата с экрана"):
        result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
        result = result_element.text.strip()

    # Декорируем проверку
    with allure.step("Проверка равенства полученного результата ожидаемому значению"):
        assert result == "15", f"Результат отличается от ожидаемого ({result})"
