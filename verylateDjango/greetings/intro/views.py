from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homePage(request):
	page = "<!DOCTYPE html>"
	page += "<html>"
	page += "<head>"
	page += "<title>Intro to Django Setup</title>"
	page += "</head>"
	page += "<body>"
	page += "<h2>Hello World!</h2>"
	page += "<p>This is the beginning of this project...</p>"
	page += "<p><a href=\"meetme\">Meet Me</a>"
	page += "</body>"
	page += "</html>"
	return HttpResponse(page)

def meetme(request):
	data = {
	"name": "Samantha Lopez", 
	"major": "Software Development", 
	"city": "New Albany"
	"hobby1": "creative writing",
	"hobby2": "music",
	"pet": "cats",
	"job": "Amazon",
	"country1": "Poland",
	"country2": "Germany",
	"country3": "Switzerland",
	"experience": "Currently, I've used programming skills in class. Mostly, I've used python to complete courses. I'm interested in game development and also in anything that might aid in helping people."
	}
	return render(request, "hiThere.html", data)



