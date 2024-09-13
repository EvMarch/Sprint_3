from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from locators import Locators
from urls_credits import Credits, Urls

def test_exit():
    driver.get(Urls.url_main)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    sleep(2)
    driver.find_element(By.XPATH, Locators.SAUCES_SECTION).click()
    sleep(2)  # Ожидание страницы
    assert Locators.SAUCES_SECTION_ACTIVE

    driver.find_element(By.XPATH, Locators.FILLINGS_SECTION).click()
    sleep(2)
    assert Locators.FILLINGS_SECTION_ACTIVE

    driver.find_element(By.XPATH, Locators.BUN_SECTION).click()
    sleep(2)  # Ожидание страницы
    assert Locators.BUN_SECTION_ACTIVE
