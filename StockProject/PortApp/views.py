from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def client(request):
    return HttpResponse('Hello')
