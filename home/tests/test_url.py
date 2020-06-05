from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import help,contact,home,open_reports,myissues
import re
import random

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
    
    def test_open_reports_url_is_resolved(self):
        url = reverse('open-reports')
        self.assertEquals(resolve(url).func,open_reports)
    
    def test_myissues_url_is_resolved(self):
        url = reverse('my-issues')
        self.assertEquals(resolve(url).func,myissues)

    def test_myissues_update_url_is_resolved(self):
        expected_url_pattern = r'\d+' + '/update/'
        for i in range(15):
            randomint = random.randint(1,1001)
        url_being_tested = '{}/update/'.format(randomint)
        self.assertTrue(re.match(expected_url_pattern,url_being_tested))