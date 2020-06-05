from django.urls import path
from . import views
from .views import myissuesUpdate, fieldsUpdate

urlpatterns = [
				path('help/',views.help, name="help-page"),
				path('contact/',views.contact, name="contact-page"),
				path('open_reports/',views.open_reports, name="open-reports"),
				path('',views.home, name="home-page"),
				path('<int:pk>/update/', myissuesUpdate.as_view(), name="my-issues-update"),
				path('myissues/',views.myissues, name="my-issues"),
				path('<int:pk>/updatefields/', fieldsUpdate.as_view(success_url="/updatefields/"), name="update-fields-form"),
				path('updatefields/',views.update_fields, name="update-fields"),
				path('admin/',views.myissues, name="admin-db"),
				
			      ]