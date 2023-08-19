from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from PIL import ImageGrab
#from .forms import PhotoForm
#, StockForm
from .models import Photos

def upload_photo(request):
    if request.method == 'POST':
        #form = StockForm(request.POST)
        form = PhotoForm(request.POST,request.FILES)
        comment_value = request.POST.get('comment','')
        stock_value = request.POST.get('stock','')
        port_value = request.POST.get('portfolio_category','')
        files = request.FILES.getlist("images")
        #s = request.POST.get('Stock','')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            
            for image in files:
                p = Photo.objects.create(
                    comment = f"{comment_value}",
                    stock_id=f'{stock_value}',
                    photo=image,
                    portfolio_category=f'{port_value}',
                    )
    
    #context = {'form': StockForm()}
    # else:
    #     #form = PhotoForm()
    context = {'form': PhotoForm()}
    return render(request, "PortApp/upload_photo.html", context)



def tradePhoto(request):




    context={}
    return render(request,'PortApp/trade_photo.html',context)

def addPhoto(request):




    context={}
    return render(request,'PortApp/add.html',context)

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
    #o = Photo.objects.get('comment,stock')

    context = {'categories': Photo.portfolio_category,'photo': Photo.photo}
    return render(request, "PortApp/show_photo.html", context)



    #img = ImageGrab.grabclipboard()
    # or ImageGrab.grab() to grab the whole screen!

   # return HttpResponse(img)
    #return HttpResponse('Hello, Guest')

# def upload_photo(request):
#     return ('hey')