from django.urls import path
#from django.views.generic import RedirectView
from . import views
from PortApp.models import Client

urlpatterns = [
    path('',views.dashboard,name = 'dashboard'),
    #path('client', views.client, name='client'),
    #path('client',Client,name = 'client')
    #path('client/client', RedirectView.as_view(url='client', permanent=False)),
]