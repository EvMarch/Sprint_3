from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Регистрация"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, REGISTER_NAME_FIELD))
    ).send_keys("Test User")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, REGISTER_EMAIL_FIELD))
    ).send_keys("testuser123@example.com")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, REGISTER_PASSWORD_FIELD))
    ).send_keys("123456")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON))
    ).click()

    # Проверка успешной регистрации может потребовать дополнительной валидации

    driver.quit()


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_BUTTON_HOME))
    ).click()

    # Дополнительные шаги для авторизации могут быть добавлены тут

    driver.quit()


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, PROFILE_BUTTON))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, CONSTRUCTOR_BUTTON))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, LOGO_BUTTON))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, LOGOUT_BUTTON))
    ).click()

    driver.quit()


def test_constructor_sections():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, PROFILE_BUTTON))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, CONSTRUCTOR_BUTTON))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, BUNS_SECTION))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, SAUCES_SECTION))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, TOPPINGS_SECTION))
    ).click()

    driver.quit()