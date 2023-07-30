from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from PIL import ImageGrab

from django.shortcuts import render, redirect
from .forms import PhotoForm

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # else:
        #     context = {'form': form}
        # return render(request, 'PortApp/upload_photo.html',context)
    context = {'form': PhotoForm()}
    return render(request, 'PortApp/upload_photo.html',context)

def intro(request):
    return HttpResponse('Welcome to Awesome Website')
def dashboard(request):

    img = ImageGrab.grabclipboard()
    # or ImageGrab.grab() to grab the whole screen!

    return HttpResponse(img)
    #return HttpResponse('Hello, Guest')

# def upload_photo(request):
#     return ('hey')