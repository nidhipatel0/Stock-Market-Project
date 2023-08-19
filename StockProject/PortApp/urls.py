from django.urls import path
#from django.views.generic import RedirectView
from . import views
from .models import Clients

urlpatterns = [
    path('upload/', views.upload_photo, name='upload_photo'),
    path('',views.intro,name = 'dashboard'),
    path('trade_photo/', views.tradePhoto,name='tradePhoto'),
    path('add/', views.addPhoto,name='addPhoto'),
    #path('/admin/PortApp/photo/add',views.upload_photo,name = 'upload_photo'),

    #path('client', views.client, name='client'),
    #path('client',Client,name = 'client')
    #path('client/client', RedirectView.as_view(url='client', permanent=False)),
]