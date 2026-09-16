from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import constants

class TestLogOut:
	def test_logout_from_personal_account(self, driver):

		# находим кнопку входа на главной странице и кликаем
		driver.find_element(*locators.SIGN_IN_FROM_MAIN_PAGE_BUTTON).click()
		# подождали чтобы форма авторизации появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		# находим поля ввода и заполняем через фикстуру
		driver.find_element(*locators.EMAIL_INPUT).send_keys(constants.existing_email)
		driver.find_element(*locators.PASSWORD_INPUT).send_keys(constants.existing_password)

		# находим кнопку Войти в форме авторизации и кликаем
		driver.find_element(*locators.SIGN_IN_SUBMIT_BUTTON).click()
		# подождали перехода на главную страницу
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.MAKE_ORDER_BUTTON)))

		# находим кнопку Личный кабинет и кликаем
		driver.find_element(*locators.ACCOUNT_BUTTON).click()
		
		# ждем чтобы страница ЛК прогрузилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.ORDERS_HISTORY)))

		# находим кнопку Выход и кликаем по ней
		driver.find_element(*locators.EXIT_BUTTON).click()

		# ждем чтобы форма авторизации появилась
		WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.AUTHORIZATION_FORM)))

		assert driver.current_url == constants.url_auth_form_page