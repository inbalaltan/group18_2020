from django.urls import path
from . import views

urlpatterns = [
    path('mifga/', views.mifga, name="mifga"),
]