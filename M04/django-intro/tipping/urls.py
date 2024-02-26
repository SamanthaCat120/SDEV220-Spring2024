from django.urls import path
from . import views


urlpatterns = [
	path("", views.homePage),
	path("simple", views.simple),
	path("tipCalc", views.inputs),
	path("results", views.calculateTip)
]

 