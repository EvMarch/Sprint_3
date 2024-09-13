from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from locators import Locators
from urls_credits import Urls, Credits


def test_cabinet_login_user(driver):

    driver.get(Urls.url_main)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()

    sleep(2)  # Ожидание страницы
    assert "Профиль" in driver.page_source  # Проверка перехода по клику в личный кабинет зарегистрированного пользователя


def test_cabinet_not_login_user(driver):

    driver.get(Urls.url_main)
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()

    sleep(2)  # Ожидание страницы
    assert "Профиль" not in driver.page_source  # Проверка перехода по клику в личный кабинет незарегистрированного пользователя

