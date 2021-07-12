from unittest.case import expectedFailure
from django import urls
from django.test import TestCase , SimpleTestCase
from django.urls import reverse


class SnakesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        actual_status_code = self.client.get(url).status_code
        expected_status_code = 200
        self.assertEqual(actual_status_code, expected_status_code)

    def test_about_page_status_code(self):
        url=reverse('about')    
        actual_status_code=self.client.get(url).status_code
        expected_status_code=200
        self.assertEqual(actual_status_code,expected_status_code)

    def test_template_use_home(self):
        url=reverse('home')    
        actual_template_name=self.client.get(url).templates[0].name
        expected_template_name='home.html'
        self.assertEqual(actual_template_name,expected_template_name)

    def test_template_use_about(self):
        url=reverse('about')    
        actual_template_name=self.client.get(url).templates[0].name
        expected_template_name='about.html'
        self.assertEqual(actual_template_name,expected_template_name)

    def test_template_use_home(self):
        url=reverse('about')    
        actual_template_name=self.client.get(url).templates[1].name
        expected_template_name='base.html'
        self.assertEqual(actual_template_name,expected_template_name)
    
    



# Create your tests here.
