"""
Python program introducting myself
"""
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
	return render(request, "intro.html", data)
