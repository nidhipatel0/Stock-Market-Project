from django.contrib import admin
from PortApp.models import Stocks,Prices,Exchanges,Currencies,Countries,Photos,Trades,Clients
# Register your models here.
admin.site.register(Stocks)
admin.site.register(Prices)
admin.site.register(Exchanges)
admin.site.register(Currencies)
admin.site.register(Countries)
admin.site.register(Trades)
admin.site.register(Photos)
admin.site.register(Clients)
