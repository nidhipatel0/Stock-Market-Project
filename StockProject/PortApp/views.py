from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def intro(request):
    return HttpResponse('Welcome to Awesome Website')
def dashboard(request):
    return HttpResponse('Hello, Guest')
