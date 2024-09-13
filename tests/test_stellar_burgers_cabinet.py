from selenium.webdriver.common.by import By
from locators import Locators
from urls_credits import Urls, Credits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

def test_cabinet_login_user(driver):

    driver.get(Urls.URL_MAIN)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
    sleep(2)
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_account__vgk_w")))  # Ожидание страницы
    assert "Профиль" in driver.page_source  # Проверка перехода по клику в личный кабинет зарегистрированного пользователя


def test_cabinet_not_login_user(driver):
    driver.get(Urls.URL_LOGIN)
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))  # Ожидание страницы
    assert "Профиль" not in driver.page_source  # Проверка перехода по клику в личный кабинет незарегистрированного пользователя

