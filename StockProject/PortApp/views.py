from django.shortcuts import render,redirect
#from django.hfilter_tradep import Hfilter_tradepResponse
# Create your views here.
'''
pip install django
pip install django-admin
pip install django-cors-headers
pip install mysqlclient
pip install slack
pip install slack_sdk
pip install tradingview_ta
pip install django-inspectdb_refactor
pip install django-rest_framework
pip install boto3
pip install django-storages
pip install ImageGrab
pip install Pillow
'''
#from PIL import ImageGrab
#from .forms import PhotoForm
#, StockForm
from PortApp.models import Stocks,Prices,Exchanges,Currencies,Countries,Photos,Trades,Clients
from rest_framework import generics
from rest_framework.response import Response
import time
import boto3
import re

from django.db.models import Q
global liq,inv
liq=100000
inv=200000
def is_valid(para):
    return para != '' and para is not None

def add_photo(request):
    # n = N.objects.all()
    # j = request.GET.get('j')
    # if j!=None:
    #     n = N.objects.filter(id=j)
    # print(n.get())
    # l = n


    context={'trades':Trades.objects.all()}
    return render(request,'PortApp/add_photo.html',context)

def recommendations(request):
    pass

def dashboard(request):#1
    trades= Trades.objects.all()
    portfolios = Trades.objects.all().values_list('portfolio',flat=True).distinct()
    context = {'trades':trades,'portfolios':portfolios}
    #o = Photo.objects.get('comment,stock')
    return render(request,'PortApp/base.html',context)


def view_port(request,port):#2
    trades= Trades.objects.filter(portfolio=port)
    context = {'trades':trades[0],}
    return render(request,'PortApp/view_port.html',context)

def view_stocks(request,sk):#3
    stocks = Stocks.objects.filter(symbol=sk)
    trades= Trades.objects.filter(stock__in=stocks) #t = Trades.objects.all()...t[0].stock #APPL
    context = {'trades':trades,}
    return render(request,'PortApp/view_stocks.html',context)


def view_trade(request,pk):#4
    trades= Trades.objects.get(id=pk)
    filter_photos = Photos.objects.filter(trade=trades.id)
    stocks = Stocks.objects.get(symbol=trades.stock)
    for filter_photo in filter_photos:
        key = filter_photo.photo.decode()
        response = boto3.client('s3').generate_presigned_url('get_object',
                                                Params={'Bucket': 'mytradeapp',
                                                        'Key': key},
                                                ExpiresIn=360000)
        
        Photos.objects.filter(photo = key).update(photo_response = response)#only decoded photo name works
    
    try:
        context={'trades':trades,'stocks':stocks,'filter_photos':filter_photos}

    except:
        context={'trades':trades,'stocks':stocks}

    return render(request,'PortApp/view_trade.html',context)

def view_photo(request,pk):
    photo= Photos.objects.get(id=pk)
    context = {'photo':photo,}
    return render(request,'PortApp/view_port.html',context)


def new_trade(request):
    trades = Trades.objects.all()
    if request.method == 'POST':

        data = request.POST
        #n_trades = request.GET.get('n_trades')
        n_photos = request.FILES.getlist('images')
        i = Stocks.objects.get(symbol=data['stock_id'])
        #print(n_photos[0])
        trades = Trades.objects.all()
        photos = Photos.objects.all()

        try:
            trade = Trades.objects.create(
                stock = i,#convets APPL tp id og stock here
                trade_comment = data['trade_comment'],
                trade_date = data['trade_date'],
                position = data['position'],
                outcome = data['outcome'],
                trade_type = data['trade_type'],
                expiry = data['expiry'],
                portfolio = 'Long term'
            )

        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
    
        if n_photos != []:
            for n_photo in n_photos:
                time_stamp = str(time.time())
                pafilter_tradeern = r'[^a-zA-Z0-9-\.]+'
                cs1 = re.sub(pafilter_tradeern, '', str(n_photo))
                cs = str(time_stamp) + cs1

                response = boto3.client("s3").put_object(Body=n_photo, Bucket="mytradeapp", Key=cs)
                
                photo = Photos.objects.create(
                    photo = cs,
                    photo_date = data['photo_date'],
                    photo_comment = data['photo_comment'],
                    trade = trade,
                )
        #return redirect('new_trade')
    context = {'trades':trades}
    return render(request,'PortApp/new_trade.html',context)

#Photos.objects.get(id=14).photo.decode()
#submit not working..works for only photo_comment


# stockID = Stocks.objects.filter(symbol=stock_symbol).values_list('id').distinct
        # tradeStockID = Trades.objects.all().values_list('stock')
        # stockId_list=[]

        # for ID in tradeStockID:
        #     if ID in stockID:
        #         stockId_list.append(ID)

        # filter_trade = Trades.objects.filter(stock__in=stockId_list)

def filter_photo(request):
    photos = Photos.objects.all()
    
    filter_trade = Trades.objects.all()
    #outcomes = t.filter((a, i) => t.findIndex((stock) => a.age === stock.age) === i)
    outcomes = Trades.objects.all().values_list('outcome',flat=True).distinct()
    photos = Trades.objects.all().values_list('portfolio',flat=True).distinct()
    #print('outcomes',outcomes)
    stock_symbol = request.GET.get('stock_symbol')
    trade_ID = request.GET.get('trade_ID')
    DOT = request.GET.get('DOT')
    outcome = request.GET.get('outcome')
    #print(t.values())
    filter_trade=[]
    if DOT == '':
        DOT='a'
    if is_valid(stock_symbol):
        stock = Stocks.objects.filter(symbol=stock_symbol).values_list('id').distinct()
        filter_stock = Trades.objects.filter(stock__in=stock)
    else:
        stock =''
    # if is_valid(trade_ID):

    #     filter_trade_ID = Trades.objects.filter(id=trade_ID)
    #     print(filter_trade.all)
        

    
    # if is_valid(DOT):
    #     filter_DOT = Trades.objects.filter(trade_date__icontains=DOT)

    
    # if is_valid(out):
    #     filter_out = Trades.objects.filter(outcome=out)
    try:
        filter_trade = Trades.objects.filter(Q(id=trade_ID) | Q(stock__in=stock) |Q(trade_date__icontains=DOT) | Q(outcome=outcome)) 
    except ValueError:
        pass
    if filter_trade!= []:
        id_list = filter_trade.values_list('id')
        filter_photos = Photos.objects.filter(trade__in=id_list)
        
        
        for filter_photo in filter_photos:
            key = filter_photo.photo.decode()
            response = boto3.client('s3').generate_presigned_url('get_object',
                                                    Params={'Bucket': 'mytradeapp',
                                                            'Key': key},
                                                    ExpiresIn=360000)
            
            Photos.objects.filter(photo = key).update(photo_response = response)#only decoded photo name works
        
    try:
        context={'filter_trade':filter_trade,'outcomes':outcomes,'filter_photos':filter_photos}
    
    except:
        context={'filter_trade':filter_trade,'outcomes':outcomes,'photos':photos}

 
    return render(request,'PortApp/filter_photo.html',context)




def trade_photo(request):
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
    return Hfilter_tradepResponse('Welcome outcomes Awesome Website')


    # context = {'categories': Photo.portfolio_category,'photo': Photo.photo}
    # return render(request, "PortApp/add_photo.html", context)



    #img = ImageGrab.grabclipboard()
    # or ImageGrab.grab() outcomes grab the whole screen!

   # return Hfilter_tradepResponse(img)
    #return Hfilter_tradepResponse('Hello, Guest')

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
        #stock = request.POST.get('Stock','')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            
            for image in files:
                photos = Photo.objects.create(
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