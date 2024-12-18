from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework.views import APIView 
from rest_framework.response import Response
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