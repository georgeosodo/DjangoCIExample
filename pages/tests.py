from django.test import TestCase


# Create your tests here.
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response= self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_has_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response,'<h1>Home page</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response,'Hi there!')


class AboutPageTests(TestCase):
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code,200)
        
    def test_about_page_returns_correct_html(self):
        response= self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About page</h1>')
        
    def test_about_pagr_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('about'))
        self.assertNotContains(response,'Hi there')
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'about.html')