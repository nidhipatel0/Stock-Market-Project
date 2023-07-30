from django.urls import path
#from django.views.generic import RedirectView
from . import views
from .models import Client

urlpatterns = [
    path('upload/', views.upload_photo, name='upload_photo'),
    path('',views.dashboard,name = 'dashboard'),
    
    #path('/admin/PortApp/photo/add',views.upload_photo,name = 'upload_photo'),

    #path('client', views.client, name='client'),
    #path('client',Client,name = 'client')
    #path('client/client', RedirectView.as_view(url='client', permanent=False)),
]