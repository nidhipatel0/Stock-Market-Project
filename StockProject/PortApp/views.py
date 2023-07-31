from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from PIL import ImageGrab
from .forms import PhotoForm
#, StockForm
from .models import Photo

def upload_photo(request):
    if request.method == 'POST':
        #form = StockForm(request.POST)
        form = PhotoForm(request.POST,request.FILES)
        files = request.FILES.getlist("photo")
        #s = request.POST.get('Stock','')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            
            for image in files:
                p = Photo.objects.create(
                    comment=form['comment'],
                    stock=form['stock'],
                    photo=image,
                )
    
    #context = {'form': StockForm()}
    # else:
    #     #form = PhotoForm()
    context = {'form': PhotoForm()}
    return render(request, "PortApp/upload_photo.html", context)







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
    o = Photo.objects.get('comment,stock')

    context = {'comment': Photo.comment}
    return render(request, "PortApp/show_photo.html", context)



    #img = ImageGrab.grabclipboard()
    # or ImageGrab.grab() to grab the whole screen!

   # return HttpResponse(img)
    #return HttpResponse('Hello, Guest')

# def upload_photo(request):
#     return ('hey')