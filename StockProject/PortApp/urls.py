from django.urls import path
#from django.views.generic import RedirectView
from . import views
#from .models import Clients

urlpatterns = [
    
    path('',views.dashboard,name = 'dashboard'),
    path('add_photo/', views.add_photo,name='add_photo'),
    path('filter_photo/', views.filter_photo,name='filter_photo'),
    path('trade_photo/', views.trade_photo,name='trade_photo'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('new_trade/', views.new_trade, name='new_trade'),
    path('view_port/<str:pk>', views.view_port, name='view_port'),
    path('view_trade/<str:pk>', views.view_trade, name='view_trade'),
    #path('/admin/PortApp/photo/add',views.upload_photo,name = 'upload_photo'),

    #path('client', views.client, name='client'),
    #path('client',Client,name = 'client')
    #path('client/client', RedirectView.as_view(url='client', permanent=False)),
]