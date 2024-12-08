from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework.views import APIView 
from rest_framework.response import Response
# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='login/')
def home(request):
    return render(request, 'dashboard/index.html') 

class GetResponse(APIView):
    def get(self, request):
        return Response({
            'message':'hello world!'
        })
