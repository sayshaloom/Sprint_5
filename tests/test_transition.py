from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators

class TestTransition:
	def test_transition_to_buns(self, driver):
		driver.find_element(*locators.DRESSINGS).click()
		WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((locators.DRESSINGS_ACTIVE)))

		driver.find_element(*locators.BUNS).click()
		WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((locators.BUNS_ACTIVE)))

		assert 'current' in driver.find_element(*locators.BUNS_DIV).get_attribute('class')

	def test_transition_to_dressings(self, driver):
		driver.find_element(*locators.DRESSINGS).click()
		WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((locators.DRESSINGS_ACTIVE)))

		assert 'current' in driver.find_element(*locators.DRESSINGS_DIV).get_attribute('class')

	def test_transition_to_fillings(self, driver):
		driver.find_element(*locators.FILLINGS).click()
		WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((locators.FILLINGS_ACTIVE)))

		assert 'current' in driver.find_element(*locators.FILLINGS_DIV).get_attribute('class')