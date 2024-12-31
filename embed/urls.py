from django.urls import path,include
from .views import *

app_name = "embed"

urlpatterns = [
    
    path('<uuid:widget_id>',  WidgetEmbed , name='widget_embed'),
    
]