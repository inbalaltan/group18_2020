from django.test import TestCase, Client
from django.urls import reverse
from mifga.models import Mifga
from django.contrib.auth.models import User
from home.views import take_obs,close_issue,change_subject
from django.test.client import RequestFactory
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware

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
        self.mifga1 = Mifga(
        title = 'unit_Test', content= 'Test test', author = self.user, 
        street = 'ביאליק', house_number = '15')
        self.mifga1.save()
        self.factory = RequestFactory()

    def test_home_GET(self):
        response = self.client.get(reverse('home-page'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_open_reports_POST(self):
        response = self.client.post(self.open_reports_url)
        self.assertEquals(response.status_code,302)


    def test_myissues(self):
        get_object = Mifga.objects.get(id = self.mifga1.id)
        response = self.client.get(reverse('my-issues'), follow= True)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(get_object, self.mifga1)
        get_object.delete()

    def test_open_issues(self):
        get_object = Mifga.objects.get(id = self.mifga1.id)
        response = self.client.get(reverse('open-reports'), follow= True)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(get_object, self.mifga1)
        get_object.delete()

    def test_take_obs_404(self):
        request = self.factory.get('home/open_reports.html')
        self.client.force_login(self.user)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = self.client.get(take_obs(request, self.mifga1.id), follow = True)
        self.assertEqual(response.status_code, 404)


    def test_close_issue_myissues_404(self):
        request = self.factory.get('home/myissues.html')
        self.client.force_login(self.user)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = self.client.get(close_issue(request, self.mifga1.id), follow = True)
        self.assertEqual(response.status_code, 404)

    def test_change_subject_myissues_404(self):
        request = self.factory.get('home/myissues.html')
        self.client.force_login(self.user)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = self.client.get(change_subject(request, self.mifga1.id,'def'), follow = True)
        self.assertEqual(response.status_code, 404)
    

