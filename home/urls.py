from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
				path('help/',views.help, name="help-page"),
				path('contact/',views.contact, name="contact-page"),
				path('open_reports/',views.open_reports, name="open-reports"),
				path('take_obs/',views.take_obs, name="take_obs"),
				path('',views.home, name="home-page"),
			      ]