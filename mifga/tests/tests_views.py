from django.test import TestCase, Client
from django.urls import reverse
from mifga.models import Mifga
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.mifga_url = reverse("mifga")
        self.user_login = {'username': 'test','password': '!!Test123'}
        self.user = User.objects.create_user(**self.user_login)
        self.user.save()
        self.mifga = Mifga(
        title = 'unit_Test', content= 'Test test', author = self.user, 
        street = 'ביאליק', house_number = '15')
        self.mifga.save()

    def test_mifga_POST(self):
        response = self.client.post(self.mifga_url)
        self.assertEquals(response.status_code,302)

    def test_mifgs_GET(self):
        self.client.force_login(self.user)
        response = self.client.get('/mifga/', follow=True)
        self.assertEqual(response.status_code, 200)
    
