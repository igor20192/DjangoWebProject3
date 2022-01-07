from django.urls import path
from test import views

urlpatterns = [path("", views.hello, name="test")]
