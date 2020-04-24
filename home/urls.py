from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
				path('help/',views.help, name="help-page"),
				path('contact/',views.contact, name="contact-page"),
				path('',views.home, name="home-page"),
			      ]