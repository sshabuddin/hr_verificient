from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def emplye(request):

	output = "This is from employe page"
	return HttpResponse(output)