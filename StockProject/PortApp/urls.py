from django.urls import path
#from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('client', views.client, name='client'),
    #path('client/client', RedirectView.as_view(url='client', permanent=False)),
]