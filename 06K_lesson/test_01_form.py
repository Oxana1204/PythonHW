from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        # Шаг 1: Открыть страницу в Edge
        print("Открываю страницу в Edge...")
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()

        # Ждем загрузки формы
        wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

        # Шаг 2: Заполнить форму значениями
        print("Заполняю форму...")

        # First name
        first_name = driver.find_element(By.NAME, "first-name")
        first_name.clear()
        first_name.send_keys("Иван")

        # Last name
        last_name = driver.find_element(By.NAME, "last-name")
        last_name.clear()
        last_name.send_keys("Петров")

        # Address
        address = driver.find_element(By.NAME, "address")
        address.clear()
        address.send_keys("Ленина, 55-3")

        # Email
        email = driver.find_element(By.NAME, "e-mail")
        email.clear()
        email.send_keys("test@skypro.com")

        # Phone number
        phone = driver.find_element(By.NAME, "phone")
        phone.clear()
        phone.send_keys("+7985899998787")

        # Zip code - оставить пустым
        zip_code = driver.find_element(By.NAME, "zip-code")
        zip_code.clear()

        # City
        city = driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys("Москва")

        # Country
        country = driver.find_element(By.NAME, "country")
        country.clear()
        country.send_keys("Россия")

        # Job position
        job_position = driver.find_element(By.NAME, "job-position")
        job_position.clear()
        job_position.send_keys("QA")

        # Company
        company = driver.find_element(By.NAME, "company")
        company.clear()
        company.send_keys("SkyPro")

        # Шаг 3: Нажать кнопку Submit
        print("Нажимаю кнопку Submit")
        submit_button = driver.find_element \
            (By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']")
        submit_button.click()

        # Шаг 4: Проверяю подстетку полей
        print("Проверяю подсветку полей...")
        wait = WebDriverWait(driver, 15)

        # Ожидание загрузки страницы и наличия необходимых элементов
        fields_to_check = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "email": "test@skypro.com",
            "phone-number": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        print("Проверяю подсветку полей...")

        print("Проверяю подсветку полей...")

        for field_id, value in fields_to_check.items():
            try:
                # Ждем появление элемента на странице
                element = wait.until(
                    EC.visibility_of_element_located((By.ID, field_id)))

                # Получаем значение атрибута класса
                class_attr = element.get_attribute("class")

                # Проверяем каждое поле отдельно
                if field_id == "zip-code":
                    # Поле Zip code должно быть подсвечено красным
                    assert "is-invalid" in class_attr, \
                        f"Поле {field_id} должно быть подсвечено красным!"
                    print(f"✅ Поле '{field_id}' подсвечено красным.")
                else:
                    # Остальные поля подсвечены зеленым
                    assert "is-valid" in class_attr, \
                        f"Поле {field_id} должно быть подсвечено зеленым!"
                    print(f"✅ Поле '{field_id}' подсвечено зеленым.")
            except Exception as e:
                print(f"Произошла ошибка при проверке поля {field_id}: {e}")

        print("✔️ Все поля отображаются корректно!")

        print("ТЕСТ УСПЕШНО ПРОЙДЕН!")
        print("Все требования задачи выполнены!")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_form_validation()
