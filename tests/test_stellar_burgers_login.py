from selenium.webdriver.common.by import By
from locators import Locators
from urls_credits import Credits, Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_login_via_main_button(driver):
    driver.get(Urls.URL_MAIN)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа по кнопке войти


def test_login_via_cabinet(driver):
    driver.get(Urls.URL_MAIN)
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа через Личный кабинет


def test_login_via_registration(driver):
    driver.get(Urls.URL_REGISTRATION)
    driver.find_element(By.XPATH, Locators.REGISTRATION_LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа через кнопку в форме регистрации


def test_login_via_forgot_password(driver):
    driver.get(Urls.URL_FORGOT_PASSWORD)
    driver.find_element(By.XPATH, Locators.REGISTRATION_LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert "Оформить заказ" in driver.page_source  # Проверка перехода на страницу входа через кнопку восстановить пароль


