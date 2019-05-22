from django.test import TestCase
from wiki.views import Page
from wiki.models import Page 

class PageTestCase(TestCase):
    def setUp(self):
        Page.objects.create(title="Test page", content ="This is a text page, purely for testing purposes.")
    def test_page_works(self):
        """ Page is created and contains a title and content"""
        Page.objects.get(title = "Test page")
        content_test = Page.objects.get(content = "This is a text page, purely for testing purposes.")
        self.assertEqual(content_test.content,"This is a text page, purely for testing purposes." )
# Create your tests here.
