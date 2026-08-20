from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests import locators

def test_transition_to_buns():
	driver = webdriver.Chrome()
	driver.get('https://stellarburgers.education-services.ru/')

	driver.find_element(*locators.DRESSINGS).click()
	WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((locators.CURRENT)))

	driver.find_element(*locators.BUNS).click()
	WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((locators.CURRENT)))

	assert 'current' in driver.find_element(*locators.DRESSINGS).find_element(By.XPATH, "./parent::div").get_attribute('class')

	driver.quit()

def test_transition_to_dressings():
	driver = webdriver.Chrome()
	driver.get('https://stellarburgers.education-services.ru/')

	driver.find_element(*locators.DRESSINGS).click()
	WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((locators.CURRENT)))

	assert 'current' in driver.find_element(*locators.DRESSINGS).find_element(By.XPATH, "./parent::div").get_attribute('class')

	# закрыли браузер
	driver.quit()

def test_transition_to_fillings():
	driver = webdriver.Chrome()
	driver.get('https://stellarburgers.education-services.ru/')

	driver.find_element(*locators.FILLINGS).click()
	WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((locators.CURRENT)))

	assert 'current' in driver.find_element(*locators.FILLINGS).find_element(By.XPATH, "./parent::div").get_attribute('class')

	# закрыли браузер
	driver.quit()