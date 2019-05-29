from django.test import TestCase, Client
from django.contrib.auth.models import User
from wiki.views import IndexView, DetailView
from wiki.models import Page
from django.urls import reverse 
from django.http import HttpRequest
# testing a page created

class PageTestCase(TestCase):
    client = Client()
    """ creates a page and a user"""
    def setUp(self):
        User.objects.create_user("TestUser19", "testuser19@wiki.com", "notmypass1")
        Page.objects.create(title="Testpage", content ="This is a text page, purely for testing purposes.")
    
    def test_page_works(self):
        """ Page is created and contains a title and content"""
        #Page.objects.get(title = "Testpage")
        content_test = Page.objects.get(content = "This is a text page, purely for testing purposes.")
        self.assertEqual(content_test.content,"This is a text page, purely for testing purposes." )
    
    def test_page_edit(self):
        """logs in to the page to edit it"""
        self.client.login(username = 'TestUser19', password = 'notmypass1')
        response = self.client.get('/wiki/Testpage/edit')
        self.assertEqual(response.status_code, 200)
     
    def test_page_save(self):
        """tests the saving feature of the wiki"""
        self.client.login(username = 'TestUser19', password = 'notmypass1')
        self.client.post('/wiki/Testpage2/save',{'Save': '', 'content':'whatever content'})
        page_test = Page.objects.get(title = "Testpage2")
        self.assertEqual(page_test.title, "Testpage2" )

    def test_page_deletion(self):
        """tests the deletion feature of the wiki"""
        self.client.login(username = 'TestUser19', password = 'notmypass1')
        self.client.post('/wiki/Testpage2/save',{'Delete': '', 'content':'whatever content'})
        self.assertRaises(Page.DoesNotExist, Page.objects.get, title= "Testpage2" )
    
    def test_page_exists(self):
        """Check if page exists"""
        response = self.client.get('/wiki/Testpage/')
        self.assertEqual(response.status_code, 200)
        
class PageTests(TestCase):
    """Check if the homepage exists"""
    client = Client()
    def test_index_page(self):
        response = self.client.get(reverse("wiki:index"))
        response.status_code
        self.assertEqual(response.status_code, 200)

class PageLoginLogoutTest(TestCase):
    client = Client()
    """Creates a user"""
    def setUp(self):
        self.user = User.objects.create_user("TestUser19", "testuser19@wiki.com", "notmypass1")
    def test_Login(self):
        """Tests the login feature"""
        self.client.login(username = 'TestUser19', password = 'notmypass1')
        response = self.client.get(reverse("wiki:index"))
        self.assertEqual(response.status_code, 200)
    def test_Logout(self):
        """Tests the logout feature"""
        self.client.login(username = 'TestUser19', password = 'notmypass1')
        response = self.client.get(reverse("wiki:logout"), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Kwik Login")
        
        




