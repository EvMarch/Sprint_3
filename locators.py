class Locators:

    # Кнопка «Войти в аккаунт»
    LOGIN_BUTTON_MAIN = ".//button[text()='Войти в аккаунт']"

    # Кнопка «Войти »
    LOGIN_BUTTON = ".//button[text()='Войти']"

    # Кнопка «Войти» в окне регистрации
    REGISTRATION_LOGIN_BUTTON = ".//a[text()='Войти']"

    # Поле «Имя»
    NAME_INPUT = ".//label[contains(text(), 'Имя')]/following-sibling::input"

    # Поле «Email»
    EMAIL_INPUT = ".//label[contains(text(), 'Email')]/following-sibling::input"

    # Поле «Пароль»
    PASSWORD_INPUT = "input[name='Пароль']"

    # Кнопка регистрации
    REGISTER_BUTTON = ".//button[text()='Зарегистрироваться']"

    # Логотип Stellar Burgers
    LOGO = ".//a"

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = "//p[text() = 'Конструктор']"

    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = "//p[text() = 'Личный Кабинет']"

    # Кнопка «Выйти»
    LOGOUT_BUTTON = ".//button[text()='Выход']"

    # Раздел «Булки»
    BUN_SECTION = "//div[1]"

    # Раздел «Соусы»
    SAUCES_SECTION = "//div[2]"

    # Раздел «Начинки»
    FILLINGS_SECTION = "//div[3]"

    #Активные состояния разделов конструктора

    BUN_SECTION_ACTIVE = "//*[text()='Булки']/div[1][contains(@class, 'current')]"
    SAUCES_SECTION_ACTIVE = "//*[text()='Соусы']/div[2][contains(@class, 'current')]"
    FILLINGS_SECTION_ACTIVE  = "//*[text()='Начинки']/div[3][contains(@class, 'current')]"
