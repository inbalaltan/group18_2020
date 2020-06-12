from django.test import TestCase, Client
from django.urls import reverse
from mifga.models import Mifga
from django.contrib.auth.models import User
from home.views import take_obs,close_issue,change_subject,change_assign
from django.test.client import RequestFactory
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.open_reports_url = reverse('open-reports')
        self.myissues_url = reverse('my-issues')
        self.user_login = {'username': 'test','password': '!!Test123'}
        self.user_staff_login = {'username': 'test_staff','password': '!!Test123'}
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
        response = self.client.get(reverse('my-issues'), follow= True)
        self.assertEquals(response.status_code, 200)


    def test_open_issues(self):
        response = self.client.get(reverse('open-reports'), follow= True)
        self.assertEquals(response.status_code, 200)


    def test_take_obs(self):
        request = self.factory.get('home/open_reports.html')
        self.client.force_login(self.user)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        self.assertEqual(self.mifga1.status, 'open')
        response = take_obs(request, self.mifga1.id)
        self.mifga1.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.mifga1.agent_att, self.user)
        self.assertEqual(self.mifga1.status, 'in progress')
        self.assertTrue(len(Mifga.objects.filter(id = self.mifga1.id)) > 0)

    def test_close_issue_myissues(self):
        request = self.factory.get('home/open_reports.html')
        self.client.force_login(self.user)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        response = close_issue(request, self.mifga1.id)
        self.mifga1.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.mifga1.status, 'closed')
        self.assertTrue(len(Mifga.objects.filter(id = self.mifga1.id)) > 0)

    def test_change_subject_myissues(self):
        request = self.factory.get('home/myissues.html')
        self.client.force_login(self.user)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = change_subject(request, self.mifga1.id, 'test')
        self.mifga1.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.mifga1.obs_title, 'test')
        self.assertTrue(len(Mifga.objects.filter(id = self.mifga1.id)) > 0)

    def test_change_assign_myissues(self):
        request = self.factory.get('home/myissues.html')
        self.client.force_login(self.user)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()
        response = change_assign(request, self.mifga1.id, self.user_staff)
        self.mifga1.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.mifga1.status, 'in progress')
        self.assertEqual(self.mifga1.agent_att, self.user_staff)
        self.assertTrue(len(Mifga.objects.filter(id = self.mifga1.id)) > 0)