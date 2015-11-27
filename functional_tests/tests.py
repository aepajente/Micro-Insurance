from django.test import LiveServerTestCase
from selenium import webdriver

class BranchTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_new_branch(self):
		self.browser.get(self.live_server_url + '/admin/')

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		self.fail('finish the test!')
