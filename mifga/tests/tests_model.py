from django.test import TestCase
from django.contrib.auth.models import User
from mifga.models import Mifga


class MifgaModelTest(TestCase):
    def setUp(self):
        self.user_login = {'username': 'test','password': '!!Test123'}
        self.user = User.objects.create_user(**self.user_login)
        self.user.save()
        self.mifga = Mifga(
        title = 'unit_Test', content= 'Test test', author = self.user, 
        street = 'ביאליק', house_number = '15')
        self.mifga.save()
        self.id = self.mifga.id

    def test_title(self):
        t_mifga = Mifga.objects.get(id = self.id)
        self.assertEqual(t_mifga.title, 'unit_Test')

    def test_title_max_length(self):
        t_mifga = Mifga.objects.get(id = self.id)
        max_length = t_mifga._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_street(self):
        t_mifga = Mifga.objects.get(id = self.id)
        self.assertEqual(t_mifga.street, 'ביאליק')

    def test_street_max_length(self):
        t_mifga = Mifga.objects.get(id = self.id)
        max_length = t_mifga._meta.get_field('street').max_length
        self.assertEqual(max_length, 15)

    def test_house_number(self):
        t_mifga = Mifga.objects.get(id = self.id)
        self.assertEqual(t_mifga.house_number, '15')

    def test_house_number_max_length(self):
        t_mifga = Mifga.objects.get(id = self.id)
        max_length = t_mifga._meta.get_field('house_number').max_length
        self.assertEqual(max_length, 3)

    def test_letter(self):
        t_mifga = Mifga.objects.get(id = self.id)
        self.assertEqual(t_mifga.letter, '0')

    def test_letter_max_length(self):
        t_mifga = Mifga.objects.get(id = self.id)
        max_length = t_mifga._meta.get_field('letter').max_length
        self.assertEqual(max_length, 1)

    def test_neighborhood(self):
        t_mifga = Mifga.objects.get(id = self.id)
        self.assertEqual(t_mifga.letter, '0')

    def test_neighborhood_max_length(self):
        t_mifga = Mifga.objects.get(id = self.id)
        max_length = t_mifga._meta.get_field('neighborhood').max_length
        self.assertEqual(max_length, 25)

    def test_status(self):
        t_mifga = Mifga.objects.get(id = self.id)
        self.assertEqual(t_mifga.status, 'open')

    def test_status_max_length(self):
        t_mifga = Mifga.objects.get(id = self.id)
        max_length = t_mifga._meta.get_field('status').max_length
        self.assertEqual(max_length, 255)

    def test_obs_title(self):
        t_mifga = Mifga.objects.get(id = self.id)
        self.assertEqual(t_mifga.obs_title, 'אחר')

    def test_obs_title_max_length(self):
        t_mifga = Mifga.objects.get(id = self.id)
        max_length = t_mifga._meta.get_field('obs_title').max_length
        self.assertEqual(max_length, 255)

    def test_title_missing_field(self):
        try:
            mifga = Mifga(
            title = None, content= 'Test test', author = self.user, 
            street = 'ביאליק', house_number = '15')
            mifga.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: mifga_mifga.title")

    def test_content_missing_field(self):
        try:
            mifga = Mifga(
            title = 'test', content= None, author = self.user, 
            street = 'ביאליק', house_number = '15')
            mifga.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: mifga_mifga.content")

    def test_author_missing_field(self):
        try:
            mifga = Mifga(
            title = 'test', content= 'test Test', author = None, 
            street = 'ביאליק', house_number = '15')
            mifga.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: mifga_mifga.author_id")

    def test_street_missing_field(self):
        try:
            mifga = Mifga(
            title = 'test', content= 'test Test', author = self.user, 
            street = None, house_number = '15')
            mifga.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: mifga_mifga.street")

    def test_house_number_missing_field(self):
        try:
            mifga = Mifga(
            title = 'test', content= 'test Test', author = self.user, 
            street = 'ביאליק', house_number = None)
            mifga.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: mifga_mifga.house_number")

