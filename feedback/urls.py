from django.urls import path,include
from .views import *

app_name = "feedback"

urlpatterns = [
    path('<str:slug>/',  ClientSpacePage.as_view() , name='space_name'),
    path('testimonials/create/', testimonial_create, name='create_testimonial'),
]