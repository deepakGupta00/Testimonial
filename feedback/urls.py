from django.urls import path,include
from .views import *



urlpatterns = [
    path('<str:space_name>/',  ClientSpacePage.as_view() , name='space_name'),
    path('testimonials/create/', testimonial_create, name='create_testimonial'),
]