from django.test import LiveServerTestCase
from selenium import webdriver

class BranchTest(LiveServerTestCase):
	fixtures = ['admin_user.json']

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_new_insurance_via_admin_site(self):
		self.browser.get(self.live_server_url + '/admin/')

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		username_field = self.browser.find_element_by_name('username')
		usrname_field.send_keys('admin')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('admin')
		password_field.send_keys(Keys.RETURN)

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)

		insurance_links = self.browser.find_elements_by_link_text('Insurance')
		self.assertEquals(len(insurance_links), 2)

		self.fail('finish the test!')
