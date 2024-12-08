from django.urls import path,include
from .views import *



urlpatterns = [
    path('feedback/<str:space_name>/',  ClientSpacePage.as_view() , name='space-name'),
    
    
]