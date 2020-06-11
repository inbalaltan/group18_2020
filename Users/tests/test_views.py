from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.open_reports_url = reverse('open-reports')
        self.myissues_url = reverse('my-issues')
        self.user_login = {'username': 'test','password': '!!Test123'}
        self.user_staff_login = {'username': 'test1','password': '!!Test123'}
        self.user = User.objects.create_user(**self.user_login)
        self.user.save()
        self.user_staff = User.objects.create_superuser(**self.user_staff_login)
        self.user_staff.save()

    def test_userissues_sort1(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'closed', 'subb': 'my'},follow=True, html=True)
        self.assertNotContains(response, 'open')
        self.assertNotContains(response, 'in progress')

    def test_user_issues_sort2(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'open', 'subb': 'my'},follow=True, html=True)
        self.assertNotContains(response, 'closed')
        self.assertNotContains(response, 'in progress')

    def test_user_issues_sort3(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'in progress', 'subb': 'my'},follow=True, html=True)
        self.assertNotContains(response, 'closed')
        self.assertNotContains(response, 'open')

    def test_userissues_sort4(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'closed', 'subb': 'alll'},follow=True, html=True)
        self.assertNotContains(response, 'open')
        self.assertNotContains(response, 'in progress')

    def test_user_issues_sort5(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'open', 'subb': 'alll'},follow=True, html=True)
        self.assertNotContains(response, 'closed')
        self.assertNotContains(response, 'in progress')

    def test_user_issues_sort6(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'in progress', 'subb': 'alll'},follow=True, html=True)
        self.assertNotContains(response, 'closed')
        self.assertNotContains(response, 'open')

    def test_userissues_sort7(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'closed', 'subb': 'subsc'},follow=True, html=True)
        self.assertNotContains(response, 'open')
        self.assertNotContains(response, 'in progress')

    def test_user_issues_sort8(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'open', 'subb': 'subsc'},follow=True, html=True)
        self.assertNotContains(response, 'closed')
        self.assertNotContains(response, 'in progress')

    def test_user_issues_sort9(self):
        self.client.login(username='user', password='danielby13')
        response = self.client.post(reverse('user-issues'), data={'sub': 'in progress', 'subb': 'subsc'},follow=True, html=True)
        self.assertNotContains(response, 'closed')
        self.assertNotContains(response, 'open')