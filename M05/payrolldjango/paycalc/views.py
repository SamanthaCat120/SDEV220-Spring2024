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

def calculateGross(request):
	data = {"name": "name", "rate": "rate", "hours": "hours", "need": "need"}
	if hours > OVERTIME_THRESHOLD:
		gross = (hours - OVERTIME_THRESHOLD) * rate * OVERTIME_MULTIPLIER + OVERTIME_THRESHOLD * rate
	else:
		gross = hours * rate
		return gross

def deductTaxes(gross):
	deduction = gross * TAX_RATE
	net = gross - deduction
	return net



















