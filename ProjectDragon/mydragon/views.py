from django.shortcuts import render
from django.http import HttpResponse
from .models import Dragon


def homePage(request):
	return render(request, "homePage.html")

def index(request):
    dragons = Dragon.objects.all()
    return render(request, 'dragons/index.html', {'dragons': dragons})



