from faker import Faker
import random
import string
import pytest
from selenium import webdriver
from locators import Locators
from urls_credits import Credits
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def user_name():
#Генерирует имя
    name = Faker(['en_US']).first_name()
    return name

@pytest.fixture(scope='session')
def user_email(user_name, domain="yandex.ru"):
    user_name = user_name.lower()  # Имя в нижнем регистре
    surname = Faker(['en_US']).last_name().lower()  # Фамилия в нижнем регистре
    kogorta_number = random.randint(1, 10)  # Случайное число от 100 до 999
    unique_number = random.randint(100, 999)  # Случайное число от 100 до 999
    email = f"{user_name}_{surname}_str{kogorta_number}_{str(unique_number)}@{domain}"  # Форматирование почты
    return email


@pytest.fixture(scope='session')
def user_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@pytest.fixture(scope='session')
def wrong_user_password():
    length = random.randint(1, 5)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#Нужно поправить: для действий с драйвером используем фикстуру (создаем файл conftest.py)
#И ключевое слово yield
#Создание и закрытие драйвера вручную в тесте не делаем

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#@pytest.fixture(scope='session')
#def ver_user(driver):
#    driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Credits.login_user)
 #   driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(Credits.password_user)
 #   driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
 #   yield driver.current_url
