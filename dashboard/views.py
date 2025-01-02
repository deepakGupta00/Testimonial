import os
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework.views import APIView 
from rest_framework.response import Response

from embed.serializers import TestimonialSerializer
from feedback.models import Testimonial
from .serializers import SpaceSerializer
from .models import *
from rest_framework import status
import ast
# Create your views here.
def index(request):
    space_page= Space.objects.all()

   
    context={
        "spaces":space_page
    }
    return render(request, 'dashboard/index.html' , context )

@login_required(login_url='login/')
def home(request):
    return render(request, 'dashboard/index.html') 

class GetResponse(APIView):
    def get(self, request):
        return Response({
            'message':'hello world!'
        })


class getProduct(APIView):
    def get(self,request, space_slug):
        getreview= Testimonial.objects.filter(space__slug=space_slug)
        space=Space.objects.get(slug=space_slug)
        print(getreview)
        context={
            "items":TestimonialSerializer(getreview, many=True).data,
            "space": space
        }
        return render(request, 'product/index.html',context )
    
    
def embed_widget(request, widget_id):
    # Fetch the widget from the database
    widget = get_object_or_404(Testimonial, id=widget_id)
    # Generate the HTML content for the widget
    content = f"<div>Widget Name: {widget.name}</div>"
    return HttpResponse(content, content_type="text/html")

# views.py
from django.shortcuts import render

def generate_embed_code(request, widget_id):
    context={"widget": {"id": widget_id}}
    return render(request, "dashboard/embed_code.html",context)



# class CreateSpace(APIView):
#     def post(self, request):
#         try


class GetSpaces(APIView):
    def get(self, request):
        try:
            
            space_page= Space.objects.get()
            
            serializer= SpaceSerializer(space_page)
            return Response(serializer.data)
            
        except Space.DoesNotExist:
            return Response({'message':"Not found!"})
        except Exception as e:
            return Response({'error': str(e)})
        
class SpaceView(APIView):
    """
    API view to handle creating or updating Space objects.
    """

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = SpaceSerializer(data=request.data)
        
        if serializer.is_valid():
            space = serializer.save()  
            return Response(
                {
                    "message": "Space created successfully.",
                    "data": SpaceSerializer(space).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, *args, **kwargs):
        space_id = kwargs.get("pk")
        try:
            space = Space.objects.get(id=space_id)
        except Space.DoesNotExist:
            return Response(
                {"message": "Space not found."}, status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = SpaceSerializer(space, data=request.data, partial=True)
        if serializer.is_valid():
            space = serializer.save() 
            return Response(
                {
                    "message": "Space updated successfully.",
                    "data": SpaceSerializer(space).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
        

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_mail_page(request):
   

    if request.method == 'POST':
        
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                print('Email sent successfully')
            except Exception as e:
                print(f'Error sending email: {e}')
        else:
            print('All fields are required')
    return HttpResponse("mail-test")


import google.generativeai as genai
def streamtext(request):

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works", stream=True)
    for chunk in response:
        print(chunk.text, end="")
    return HttpResponse("streamtext")