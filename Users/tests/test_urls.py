from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    def test_profile_url(self):
        response = self.client.get(reverse('profile'), follow= True)
        self.assertEquals(response.status_code, 200)

    def test_userissues_url(self):
        response = self.client.get(reverse('user-issues'), follow= True)
        self.assertEquals(response.status_code, 200)

    def test_all_reports_url(self):
        response = self.client.get(reverse('all-reports'), follow= True)
        self.assertEquals(response.status_code, 200)

    def test_change_password_url(self):
        response = self.client.get(reverse('change_password'), follow= True)
        self.assertEquals(response.status_code, 200) 

    def test_register_url(self):
        response = self.client.get(reverse('register'), follow= True)
        self.assertEquals(response.status_code, 200)  

