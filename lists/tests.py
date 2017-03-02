from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do Lists</title>', html)
		self.assertTrue(html.endswith('</html>'))

