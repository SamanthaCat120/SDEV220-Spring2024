from django.urls import path
from . import views


urlpatterns = [
    path("", views.homePage),
    path("simple", views.simple),
    path("needdamoney", views.inputs),
    path("results", views.calculatePay),
]