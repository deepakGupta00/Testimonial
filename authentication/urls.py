
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    path('',  home , name='home'),
    path('login/', login , name='login' ),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
    path('user-logout', logout_view , name='user-logout'), 
     
    
]
