from django.test import TestCase, Client
from django.contrib.auth.models import User
from mifga.models import Mifga
from home.views import send_email
from django.core import mail
import time

class EmailTest(TestCase):
    def setUp(self):
        self.user_login = {'username': 'test','password': '!!Test123','email': 'test@test.com'}
        self.user = User.objects.create_user(**self.user_login)
        self.user.save()
        self.mifga = Mifga(
        title = 'unit_Test_email', content= 'Test test', author = self.user, 
        street = 'ביאליק', house_number = '15')
        self.mifga.save()
        self.id = self.mifga.id
        self.client = Client()

    def test_check_email_outbox(self):
        with self.settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):
            send_email(self.user.email, self.mifga.status)
            time.sleep(0.5)
            self.assertEquals(len(mail.outbox), 1)
            self.assertEquals(mail.outbox[0].subject, 'Your report status has been updated')
  

