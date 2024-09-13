class Locators:
    # Заголовок страницы
    TITLE = "h1"

    # Кнопка «Войти в аккаунт»
    LOGIN_BUTTON_MAIN = ".//button[text()='Войти в аккаунт']"

    # Кнопка «Войти »
    LOGIN_BUTTON = ".//button[text()='Войти']"

    # Кнопка «Войти» в окне регистрации
    REGISTRATION_LOGIN_BUTTON = "//*[@id='root']/div/main/div/div/p/a"

    #Кнопка Восстановить пароль
    FORGOT_PASSWORD_BUTTON = "//*[@id='root']/div/main/div/div/p[2]/a"

    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = "//*[@id='root']/div/header/nav/a"

    # Поле «Имя»
    NAME_INPUT = ".//label[contains(text(), 'Имя')]/following-sibling::input"

    # Поле «Email»
    EMAIL_INPUT = ".//label[contains(text(), 'Email')]/following-sibling::input"

    # Поле «Пароль»
    PASSWORD_INPUT = "input[name='Пароль']"

    # Кнопка регистрации
    REGISTER_BUTTON = "//*[@id='root']/div/main/div/div/p[1]/a"

    # Логотип Stellar Burgers
    LOGO = "//*[@id='root']/div/header/nav/div/a"

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = "//*[@id='root']/div/header/nav/ul/li[1]/a/p"

    # Кнопка «Выйти»
    LOGOUT_BUTTON = "//*[@id = 'root']/div/main/div/nav/ul/li[3]/button"

    # Раздел «Булки»
    BUN_SECTION = "//*[@id='root']/div/main/section[1]/div[1]/div[1]"

    # Раздел «Соусы»
    SAUCES_SECTION = "//*[@id='root']/div/main/section[1]/div[1]/div[2]"

    # Раздел «Начинки»
    FILLINGS_SECTION = "//*[@id='root']/div/main/section[1]/div[1]/div[3]"

    #Активные состояния разделов конструктора

    BUN_SECTION_ACTIVE = "//*[text()='Булки']/div[1][contains(@class, 'current')]"
    SAUCES_SECTION_ACTIVE = "//*[text()='Соусы']/div[2][contains(@class, 'current')]"
    FILLINGS_SECTION_ACTIVE  = "//*[text()='Начинки']/div[3][contains(@class, 'current')]"
