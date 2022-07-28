from boohoo import Boohoo
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
import unittest
import time
import os

class BoohooTestCase(unittest.TestCase):
	def setUp(self):
		self.boohoo = Boohoo()
		self.boohoo.driver.get(self.boohoo.url)

	# def test_driver(self):
	# 	# Checks driver is going to the url that was provide
	# 	expected_value = 'https://www.boohoo.com/womens'
	# 	actual_value = self.boohoo.driver.current_url
	# 	self.assertEqual(expected_value, actual_value)

	# def test_accept_cookies(self):
	# 	self.boohoo.accept_cookies()
	# 	time.sleep(2)
	# 	cookies = self.boohoo.driver.find_element(By.ID, 'consent-dialog')
	# 	is_active = "m-visible" not in cookies.get_attribute("class")
	# 	self.assertTrue(is_active)

	# def test_create_directory(self):
	# 	self.boohoo.create_directory()
	# 	directory = ['Raw_Data', 'Images', 'Links']
	# 	cwd = os.getcwd()
	# 	for items in directory:
	# 		path = os.path.join(cwd, items)
	# 		self.assertTrue(os.path.exists(path))


	def test_navigate(self):
		self.boohoo.navigate()
		all_clothing = self.boohoo.driver.find_element(By.XPATH, '(//li/a[@class="b-menu_bar-tab_content_link m-has-submenu "])[3]')
		print(all_clothing)
		area_expanded = "true" in all_clothing.get_attribute("aria-expanded")
		self.assertTrue(area_expanded)
		

	# def test_get_categories(self):
	# 	pass
		

	# def test_click_category(self):
	# 	expected_value = 'https://www.boohoo.com/womens/dresses'
	# 	actual_value = self.driver.current_url	
	# 	self.assertEqual(expected_value, actual_value)

	# def test_get_details(self):
	# 	pass
	
	def tearDown(self):
		self.boohoo.driver.quit()

	

if __name__ == '__main__':
	unittest.main()

