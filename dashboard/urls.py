from django.urls import path,include
from .views import *



urlpatterns = [
    path('',  home , name='home'),
    path('index',  index , name='index'),
    
    path('get-response', GetResponse.as_view(), name='get-response' ),
    
    
]