from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import help,contact,home


class TestUrls(SimpleTestCase):

    def test_help_url_is_resolved(self):
        url = reverse('help-page')
        self.assertEquals(resolve(url).func,help)

    def test_contact_url_is_resolved(self):
        url = reverse('contact-page')
        self.assertEquals(resolve(url).func,contact)

    def test_home_url_is_resolved(self):
        url = reverse('home-page')
        self.assertEquals(resolve(url).func,home)
    