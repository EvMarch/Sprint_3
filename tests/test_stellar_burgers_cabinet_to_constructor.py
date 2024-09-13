from selenium.webdriver.common.by import By
from locators import Locators
from urls_credits import Credits, Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_cabinet_constructor(driver):
    driver.get(Urls.URL_MAIN)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert "Соберите бургер" in driver.page_source  # Проверка перехода из личного кабинета по клику на Конструктор


def test_cabinet_logo(driver):
    driver.get(Urls.URL_MAIN)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, Locators.LOGO).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert "Соберите бургер" in driver.page_source  # Проверка перехода из личного кабинета по клику на Конструктор
