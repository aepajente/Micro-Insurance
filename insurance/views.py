from django.shortcuts import render
from django.http import HttpResponse
from insurance.models import Branch, Underwriter, Product

def home(request):
	return render(request, 'home.html')
