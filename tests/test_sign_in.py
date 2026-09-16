from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import constants

class TestSignIn:
	def test_login_from_main_page(self, driver):

		# находим кнопку входа на главной странице и кликаем
		driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()
		# подождали, чтобы форма авторизации появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим поля ввода и заполняем
		driver.find_element(*locators.EMAIL_INPUT).send_keys(constants.existing_email)
		driver.find_element(*locators.PASSWORD_INPUT).send_keys(constants.existing_password)

		# находим кнопку Войти в форме авторизации и кликаем
		driver.find_element(*locators.SIGN_IN_SUBMIT_BUTTON).click()

		# подождали перехода на главную страницу
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.MAKE_ORDER_BUTTON)))

		assert driver.current_url == constants.url

	def test_sign_in_from_account(self, driver):

		# находим кнопку Личный кабинет и кликаем
		driver.find_element(*locators.ACCOUNT_BUTTON).click()

		# подождали, чтобы форма авторизации появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим поля ввода и заполняем
		driver.find_element(*locators.EMAIL_INPUT).send_keys(constants.existing_email)
		driver.find_element(*locators.PASSWORD_INPUT).send_keys(constants.existing_password)

		# находим кнопку Войти в форме авторизации и кликаем
		driver.find_element(*locators.SIGN_IN_SUBMIT_BUTTON).click()

		# подождали перехода на главную страницу
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.MAKE_ORDER_BUTTON)))

		assert driver.current_url == constants.url

	def test_sign_in_from_registration_form(self, driver):

		# находим кнопку входа на главной странице и кликаем
		driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()

		# подождали, чтобы форма авторизации появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим ссылку Зарегистрироваться и кликаем
		driver.find_element(*locators.REGISTRATION_LINK).click()

		# подождали чтобы форма регистрации появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.REGISTRATION_FORM)))

		# находим ссылку Войти и кликаем
		driver.find_element(*locators.SIGN_IN_LINK).click()

		# подождали, чтобы форма авторизации снова появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим поля ввода и заполняем
		driver.find_element(*locators.EMAIL_INPUT).send_keys(constants.existing_email)
		driver.find_element(*locators.PASSWORD_INPUT).send_keys(constants.existing_password)

		# находим кнопку Войти в форме авторизации и кликаем
		driver.find_element(*locators.SIGN_IN_SUBMIT_BUTTON).click()

		# подождали перехода на главную страницу
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.MAKE_ORDER_BUTTON)))

		assert driver.current_url == constants.url

	def test_sign_in_from_reset_password(self, driver):

		# находим кнопку входа на главной странице и кликаем
		driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()

		# подождали, чтобы форма авторизации появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))
 
		# находим ссылку Восстановить пароль и кликаем
		driver.find_element(*locators.FORGOR_PASSWORD_LINK).click()

		# ждем появления формы восстановления пароля
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.RESET_PASSWORD_FORM)))	
	
		# находим ссылку Войти и кликаем
		driver.find_element(*locators.SIGN_IN_LINK).click()

   		# подождали пока форма авторизации опять появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим поля ввода и заполняем
		driver.find_element(*locators.EMAIL_INPUT).send_keys(constants.existing_email)
		driver.find_element(*locators.PASSWORD_INPUT).send_keys(constants.existing_password)

		# находим кнопку Войти в форме авторизации и кликаем
		driver.find_element(*locators.SIGN_IN_SUBMIT_BUTTON).click()

		# подождали перехода на главную страницу
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.MAKE_ORDER_BUTTON)))

		assert driver.current_url == constants.url