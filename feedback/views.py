from django.shortcuts import render
from feedback.serializers import SpaceSerializers
from dashboard.models import Space
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.utils.text import slugify
import ast
class ClientSpacePage(APIView):
    def get(self, request, space_name):
        try:
            
            space_page= Space.objects.get(slug=slugify(space_name))
            
            serializer= SpaceSerializers(space_page)
            data= serializer.data
         
            data['questions']= ast.literal_eval(data['questions'])
            
          
            context = {
                "data": data
            }
            return render(request , 'feedback/index.html' ,context)
            
        except Space.DoesNotExist:
            return Response({'message':"Not found!"})
        except Exception as e:
            return Response({'error': str(e)})
       