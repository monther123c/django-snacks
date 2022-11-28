from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SnacksTest(SimpleTestCase):

    def test_home_page(self):
        url=reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
    def test_about_page(self):
        url=reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
