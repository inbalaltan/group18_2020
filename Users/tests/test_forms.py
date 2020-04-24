from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestForms(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_login = {'username': 'test','password': '!!Test123'}
        self.users = {'username': 'test','email': 'test@gmail.com','first_name':'test','last_name':'test','password1':'!!Test123','password2':'!!Test123'}
        return super().setUp()

class registerTest(TestForms): 
    def test_reg(self):
        response = self.client.post(self.register_url, self.users, format = 'text/html')
        self.assertEqual(response.status_code, 302)

class loginTest(TestForms): 
    def test_login(self):
        User.objects.create_user(**self.user_login)
        response = self.client.post(self.login_url, self.user_login, follow=True)
        self.assertTrue(response.context['user'].is_active)

class logoutTest(TestForms): 
    def test_logout(self):
        User.objects.create_user(**self.user_login)
        response = self.client.get(self.logout_url)
        self.assertFalse(response.context['user'].is_active)