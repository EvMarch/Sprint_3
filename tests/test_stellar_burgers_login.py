
from selenium.webdriver.common.by import By
from time import sleep
from locators import Locators
from urls_credits import Credits, Urls


def test_login_via_main_button(driver):
    driver.get(Urls.url_main)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    sleep(2)  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа по кнопке войти


def test_login_via_cabinet(driver):
    driver.get(Urls.url_main)
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    sleep(2)  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа через Личный кабинет


def test_login_via_registration(driver):
    driver.get(Urls.url_registration)
    driver.find_element(By.XPATH, Locators.REGISTRATION_LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    sleep(2)  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа через кнопку в форме регистрации


def test_login_via_forgot_password(driver):
    driver.get(Urls.url_forgot_password)
    driver.find_element(By.XPATH, Locators.REGISTRATION_LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    sleep(2)  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа через кнопку восстановить пароль


