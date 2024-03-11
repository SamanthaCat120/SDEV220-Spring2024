from django.urls import path
from . import views


urlpatterns = [
    path("", views.homePage),
    path("simple", views.simple),
    path("petdragon", views.inputs)
]