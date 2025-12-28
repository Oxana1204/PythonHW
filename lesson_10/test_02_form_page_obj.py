import pytest
from selenium import webdriver
from FormPage import FormPage
import allure  # импортируем модуль allure


@pytest.fixture
def driver():
    with allure.step("Запуск браузера"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()


# Добавляем аттрибуты для теста
@allure.title("Проверка прохождения формы")
@allure.description("Тестируем заполнение и отправку формы")
@allure.feature("Форма регистрации")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    form_page = FormPage(driver)

    with allure.step("Открываем страницу формы"):
        form_page.open()

    with allure.step("Заполняем форму"):
        form_page.fill_form()
        form_page.submit_form()

    with allure.step("Проверяем успешную отправку формы"):
         form_page.check_form_submission()
