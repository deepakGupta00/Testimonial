from django.urls import path,include
from .views import *

app_name="dashboard"

urlpatterns = [
    path('',  home , name='home'),
    path('index',  index , name='index'),
    path('get-spaces/', GetSpaces.as_view(), name='get-spaces' ),
    path("create-spaces/", SpaceView.as_view(), name="space-create"), 
    path("spaces/<uuid:pk>/", SpaceView.as_view(), name="space-update"),
    
    path('get-response', GetResponse.as_view(), name='get-response' ),
    
    path('product/<str:space_slug>', getProduct.as_view(), name='get_product_review'),
    
    path('embed/<uuid:widget_id>', generate_embed_code, name='embed_widget'),
    
    path('mail-test',send_mail_page, name='mail-test'),
    
    path('textstream',streamtext, name='textstream'),
]