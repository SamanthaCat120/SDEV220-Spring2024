from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homePage(request):
    page = "<!DOCTYPE html>"
    page += "<html>"
    page += "<head></head>"
    page += "<body>"
    page += "<h3> Hello World!!!</h3>"
    page += "<p>this is our first django example</p>"
    page += "<p><a href=\"tipCalc\">the actual app</a></p>"
    page += "<p><a href=\"simple\">a simple example</a></p>"
    page += "</body>"
    page += "</html>"
    return HttpResponse(page)

def simple(request):
    data = {"title": "Simple Template", "message": "Hello World"}
    return render(request, "simple.html", data)

def inputs(request):
    return render(request, "tipCalc.html")

def calculateTip(request):
    price = float(request.POST.get("price"))
    satisfaction = int(request.POST.get("satisfaction"))/100
    tip_amount = price * satisfaction
    total = price + tip_amount
    return render(request, "results.html", { "tip_amount": format(tip_amount, ".2f"), "total": format(total, ".2f") })

































