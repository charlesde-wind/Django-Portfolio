
from django.urls import path, include
from . import views

app_name = "about_me"

urlpatterns = [
    path("", views.about, name="aboutme")
]