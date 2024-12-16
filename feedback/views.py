from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from feedback.serializers import SpaceSerializers
from dashboard.models import Space
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.utils.text import slugify
import ast
from .models import TestimonialImage
from .form import TestimonialForm
from django.contrib import messages


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
    


def testimonial_create(request):
    try:
        
        if request.method=="POST":
            form = TestimonialForm(request.POST, request.FILES)
            
            if form.is_valid():
                try:
                    testimonial=form.save(commit=False)
                    testimonial.save()
                    for image in request.FILES.getlist('additional_images'):
                        testimonial_image=TestimonialImage.objects.create(image=image)
                        testimonial.additional_images.add(testimonial_image)
                    messages.success(request,"Testimonial created successfully!")
                    return redirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    messages.error(request, f"An error occurred: {e}")
                
            messages.error(request, "Please correct the errors in the form.")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
          
            form = TestimonialForm()
        return render(request, 'feedback/index.html', {'form':form})
    
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        print(f'error : {e}')