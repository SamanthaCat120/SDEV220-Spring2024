from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homePage(request):
	return render(request, "homePage.html")


def simple(request):
	data = {"title": "Simple Template", "message": "Hello World"}
	return render(request, "simple.html", data)

def inputs(request):
	return render(request, "payroll.html")

def calculatePay(request):
	return render(request, "payroll.html")



















