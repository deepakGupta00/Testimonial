from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from embed.serializers import TestimonialSerializer
from feedback.models import Testimonial

# Create your views here.
def WidgetEmbed(request, widget_id):
    widget = get_object_or_404(Testimonial, id=widget_id)
  
    context = {
               
               "widget": TestimonialSerializer(widget).data
               
    }
    return render(request, "dashboard/embed_code.html",context)
    # return HttpResponse(content, content_type="text/html")