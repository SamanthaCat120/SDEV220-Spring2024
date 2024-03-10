from django.urls import path
from . import views


urlpatterns = [
    path("", views.homePage),
    path("simple", views.simple),
    path("payroll", views.inputs),
    path('results.html', views.calculatePay, name='calculatePay'),
]