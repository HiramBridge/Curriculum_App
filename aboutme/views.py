from django.shortcuts import render

# Create your views here.


def AboutMe(request):
	return render(request, 'aboutme/aboutme.html',{})