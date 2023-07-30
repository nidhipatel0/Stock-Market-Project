from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from PIL import ImageGrab
from .forms import PhotoForm, StockForm
from .models import Photo, Stock

def upload_photo(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        files = request.FILES.getlist("photo")
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                Photo.objects.create(stock=f, photo=i)
    
    #context = {'form': StockForm()}
    else:
        form = StockForm()
        photoform = PhotoForm()
    return render(request, "PortApp/upload_photo.html", {"form":form,"photoform":photoform})




















# from django.shortcuts import render, redirect
# from .forms import PhotoForm
# from .models import Photo


# def upload_photo(request):
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         file = request.FILES.getlist('photo')
#         if form.is_valid():
#             f = form.save(commit=False)
#             f.user = request.user
#             f.save()
#             for image in file:
#                 Photo.objects.create(stock = f,photo=image)
#     # else:
#     #     form = PhotoForm()

#     context = {'form': PhotoForm()}
#     return render(request, 'PortApp/upload_photo.html',context)

def intro(request):
    return HttpResponse('Welcome to Awesome Website')
def dashboard(request):

    img = ImageGrab.grabclipboard()
    # or ImageGrab.grab() to grab the whole screen!

    return HttpResponse(img)
    #return HttpResponse('Hello, Guest')

# def upload_photo(request):
#     return ('hey')