from django.shortcuts import render

def index(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def activity(request):
	return render(request, 'activity.html')

def contact(request):
	return render(request, 'contact.html')

# Create your views here.
