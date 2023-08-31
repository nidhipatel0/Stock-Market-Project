from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from PIL import ImageGrab
#from .forms import PhotoForm
#, StockForm
from PortApp.models import Stocks,Prices,Exchanges,Currencies,Countries,Photos,Trades,Clients
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

def is_valid(para):
    return para != '' and para is not None

def add_photo(request):

    context={'trades':Trades}
    return render(request,'PortApp/add_photo.html',context)



def filter_photo(request):
    trade = Trades.objects.all
    ss = request.GET.get('stock_symbol')
    trade_ID = request.GET.get('trade_ID')
    DOT = request.GET.get('DOT')
    out = request.GET.get('outcome')

    if is_valid(ss):
        trade.filter(stock__icontains=ss)

    if is_valid(trade_ID):
        trade.filter(id=trade_ID)

    
    if is_valid(DOT):
        trade.filter(trade_date__icontains=DOT)

    
    if is_valid(out):
        trade.filter(outcome=out)


    
    context={'trades':trade}
    return render(request,'PortApp/filter_photo.html',context)




def trade_Photo(request):

    context={}
    return render(request,'PortApp/trade_photo.html',context)




def upload_photo(request):

    pass
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
    pass

    # context = {'categories': Photo.portfolio_category,'photo': Photo.photo}
    # return render(request, "PortApp/add_photo.html", context)



    #img = ImageGrab.grabclipboard()
    # or ImageGrab.grab() to grab the whole screen!

   # return HttpResponse(img)
    #return HttpResponse('Hello, Guest')

# def upload_photo(request):
#     return ('hey')










'''

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
    return render(request, "PortApp/upload_photo.html", context)'''