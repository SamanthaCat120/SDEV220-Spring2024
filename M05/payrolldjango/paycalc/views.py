from django.shortcuts import render
from django.http import HttpResponse

TAX_RATE = 0.14
OVERTIME_THRESHOLD = 40
OVERTIME_MULTIPLIER = 1.5

def homePage(request):
    return render(request, "homePage.html")

def simple(request):
    data = {"title": "Simple Template", "message": "Hello World"}
    return render(request, "simple.html", data)

def inputs(request):
    return render(request, "payroll.html")

def calculatePay(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        hours = float(request.GET.get('hours', 0))
        rate = float(request.GET.get('rate', 0))
        need = float(request.GET.get('need', 0))

        gross = calculateGross(hours, rate)

        net = deductTaxes(gross)

        return render(request, "results.html", {'name': name, 'gross': gross, 'net': net, 'need': need})

    return HttpResponse("Invalid request method")

def calculateGross(hours, rate):
    if hours > OVERTIME_THRESHOLD:
        gross = (hours - OVERTIME_THRESHOLD) * rate * OVERTIME_MULTIPLIER + OVERTIME_THRESHOLD * rate
    else:
        gross = hours * rate
    return gross

def deductTaxes(gross):
    deduction = gross * TAX_RATE
    net = gross - deduction
    return net
