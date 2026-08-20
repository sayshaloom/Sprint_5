from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests import locators

def test_successful_registration(user_data):
	driver = webdriver.Chrome()
	driver.get('https://stellarburgers.education-services.ru/')

	# находим кнопку входа на главной странице и кликаем
	driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()
	# подождали, чтобы форма авторизации появилась
	WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

	# находим ссылку регистрации и кликаем
	driver.find_element(*locators.REGISTRATION_LINK).click()
	# подождали, чтобы форма регистрации появилась
	WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.REGISTRATION_FORM)))

	# заполняем поля ввода данными

	driver.find_element(*locators.NAME_INPUT).send_keys("Робот-доставщик")
	driver.find_element(*locators.EMAIL_INPUT).send_keys(user_data["email"])
	driver.find_element(*locators.PASSWORD_INPUT).send_keys(user_data["password"])

	driver.find_element(*locators.SIGN_UP_BUTTON).click()
	WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

	assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

	driver.quit()


def test_registration_short_password_error(user_data):
	driver = webdriver.Chrome()
	driver.get('https://stellarburgers.education-services.ru/')

	# находим кнопку входа на главной странице и кликаем
	driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()
	# подождали, чтобы форма авторизации появилась
	WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

	# находим ссылку регистрации и кликаем
	driver.find_element(*locators.REGISTRATION_LINK).click()
	# подождали, чтобы форма авторизации появилась
	WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.REGISTRATION_FORM)))

	driver.find_element(*locators.NAME_INPUT).send_keys("Робот-доставщик")
	driver.find_element(*locators.EMAIL_INPUT).send_keys(user_data["email"])
	driver.find_element(*locators.PASSWORD_INPUT).send_keys("12345")

	driver.find_element(*locators.SIGN_UP_BUTTON).click()

	error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.ERROR_PASSWORD)))

	assert error_message.is_displayed()

	driver.quit()