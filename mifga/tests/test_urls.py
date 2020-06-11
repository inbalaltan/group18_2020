from django.test import SimpleTestCase
from django.urls import reverse,resolve
from mifga.views import mifga


class TestUrls(SimpleTestCase):
    
    def test_mifga_url_is_resolved(self):
        url = reverse('mifga')
        self.assertEquals(resolve(url).func, mifga)

    
    
