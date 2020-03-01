from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def employe(request):

	output = "This is from employe page"
	return HttpResponse(output)