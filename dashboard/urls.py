from django.urls import path,include
from .views import *



urlpatterns = [
    path('',  home , name='home'),
    path('index',  index , name='index'),
    path('get-spaces/', GetSpaces.as_view(), name='get-spaces' ),
    path("create-spaces/", SpaceView.as_view(), name="space-create"), 
    path("spaces/<uuid:pk>/", SpaceView.as_view(), name="space-update"),
    
    path('get-response', GetResponse.as_view(), name='get-response' ),
    
    
]