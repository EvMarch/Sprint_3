from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import Locators
from urls_credits import Urls
from selenium.webdriver.support.ui import WebDriverWait


def test_successful_registration(user_name, user_email, user_password, driver):

    driver.get(Urls.URL_REGISTRATION)
    # Заполнение формы регистрации
    driver.find_element(By.XPATH, Locators.NAME_INPUT).send_keys(user_name)
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(user_password)
    driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey"))) # Ожидание для записи результата
    assert "Войти" in driver.page_source  # Проверка успешной регистрации


def test_invalid_password_registration(user_name, user_email, wrong_user_password, driver):

    driver.get(Urls.URL_REGISTRATION)
    # Заполнение формы регистрации с некорректным паролем
    driver.find_element(By.XPATH, Locators.NAME_INPUT).send_keys(user_name)
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(wrong_user_password)
    driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))  # Ожидание для записи результата
    assert "Некорректный пароль" in driver.page_source  # Проверка на наличие сообщения об ошибке


