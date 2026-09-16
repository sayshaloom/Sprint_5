from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import helpers
import constants

class TestRegistration:
	def test_successful_registration(self, driver):

		# находим кнопку входа на главной странице и кликаем
		driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()
		# подождали, чтобы форма авторизации появилась
		WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим ссылку регистрации и кликаем
		driver.find_element(*locators.REGISTRATION_LINK).click()
		# подождали, чтобы форма регистрации появилась
		WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.REGISTRATION_FORM)))

		# заполнили форму регистрации и кликнули кнопку Зарегистрироваться
		driver.find_element(*locators.NAME_INPUT).send_keys(constants.name)
		driver.find_element(*locators.EMAIL_INPUT).send_keys(helpers.generate_random_email())
		driver.find_element(*locators.PASSWORD_INPUT).send_keys(helpers.generate_random_password())

		driver.find_element(*locators.SIGN_UP_BUTTON).click()
		# подождали, чтобы форма авторизации появилась
		WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		assert driver.current_url == constants.url_auth_form_page

	def test_registration_short_password_error(self, driver):

		# находим кнопку входа на главной странице и кликаем
		driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()
		# подождали, чтобы форма авторизации появилась
		WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим ссылку регистрации и кликаем
		driver.find_element(*locators.REGISTRATION_LINK).click()
		# подождали, чтобы форма регистрации появилась
		WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.REGISTRATION_FORM)))

		# заполнили форму регистрации с коротким паролем и кликнули кнопку Зарегистрироваться
		driver.find_element(*locators.NAME_INPUT).send_keys(constants.name)
		driver.find_element(*locators.EMAIL_INPUT).send_keys(helpers.generate_random_email())
		driver.find_element(*locators.PASSWORD_INPUT).send_keys("12345")

		driver.find_element(*locators.SIGN_UP_BUTTON).click()

		# проверка и взаимодействие с элементом-маркером успеха
		assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ERROR_PASSWORD)).is_displayed()