from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from locators import Locators
from urls_credits import Credits, Urls

def test_constructor():
    driver.get(Urls.url_main)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    assert "Вход" in driver.page_source  # Проверка выхода из аккаунта

