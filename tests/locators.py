from selenium.webdriver.common.by import By

# локаторы для test_registration
SIGN_IN_FROM_MAIN_PAGE_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
AUTHORIZATION_FORM = (By.XPATH, ".//h2[text()='Вход']")
REGISTRATION_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
REGISTRATION_FORM = (By.XPATH, ".//h2[text()='Регистрация']")
NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
SIGN_UP_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
ERROR_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")
MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
SIGN_IN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")
ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']")
SIGN_IN_LINK = (By.XPATH, ".//a[@href='/login']")
FORGOR_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']")
RESET_PASSWORD_FORM = (By.XPATH, ".//h2[text()='Восстановление пароля']")
ORDERS_HISTORY = (By.XPATH, ".//a[@href='/account/order-history']")
EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")


# локаторы для test_transition
BUNS = (By.XPATH, ".//span[text()='Булки']")
DRESSINGS = (By.XPATH, ".//span[text()='Соусы']")
FILLINGS = (By.XPATH, ".//span[text()='Начинки']")
CURRENT = (By.XPATH, ".//div[contains(@class, 'current')]")
