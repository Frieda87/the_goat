from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolces_to_home_page_view(self):
        # resolve is the function Django uses internally to resolve
        # URLs and find what view function they should map to
        found = resolve('/')
        self.assertEqual(found.func, home_page)