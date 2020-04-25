from django.test import SimpleTestCase

from django.urls import reverse,resolve
from Users.views import register


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,register)
