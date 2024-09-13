from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from urls_credits import Credits, Urls

def test_constructor(driver):
    driver.get(Urls.URL_MAIN)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.LOGIN_USER)
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.PASSWORD_USER)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))
    driver.find_element(By.XPATH, Locators.SAUCES_SECTION).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert Locators.SAUCES_SECTION_ACTIVE

    driver.find_element(By.XPATH, Locators.FILLINGS_SECTION).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))
    assert Locators.FILLINGS_SECTION_ACTIVE

    driver.find_element(By.XPATH, Locators.BUN_SECTION).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))  # Ожидание страницы
    assert Locators.BUN_SECTION_ACTIVE
