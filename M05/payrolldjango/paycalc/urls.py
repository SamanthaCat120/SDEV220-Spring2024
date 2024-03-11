from django.urls import path
from . import views


urlpatterns = [
    path("", views.homePage),
    path('simple.html', views.simple, name='simple'),
    path('payroll.html', views.inputs, name='inputs'),
    path('results.html', views.calculatePay, name='calculatePay'),
]