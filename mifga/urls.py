from django.urls import path
from . import views

urlpatterns = [
    path('miifga/', views.mifga, name="mifga"),
]