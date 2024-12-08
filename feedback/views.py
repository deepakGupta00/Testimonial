from django.shortcuts import render
from feedback.serializers import SpaceSerializers
from dashboard.models import Space
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.utils.text import slugify

class ClientSpacePage(APIView):
    def get(self, request, space_name):
        try:
            
            space_page= Space.objects.filter(slug=slugify(space_name))
            
            serializer= SpaceSerializers(space_page, many=True)
            return Response(serializer.data)
            
        except Space.DoesNotExist:
            return Response({'message':"Not found!"})
        except Exception as e:
            return Response({'error': str(e)})