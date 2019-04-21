from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	my_context= {
		"my_html" : "<h1>Hello World</h1>",
		"my_text" : "This is about us",
		"my_number": 123,
		"my_list" : [123, 456, 312, "abc"]
		
	}
	return render(request, "contact.html", my_context)

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})