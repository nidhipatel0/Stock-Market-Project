from django.contrib import admin
from PortApp.models import Stock,Price,Exchange,Currency,Country
# Register your models here.
admin.site.register(Stock)
admin.site.register(Price)
admin.site.register(Exchange)
admin.site.register(Currency)
admin.site.register(Country)
