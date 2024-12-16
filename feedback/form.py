from django import forms
from .models import Testimonial

# class TestimonialForm(forms.ModelForm):
#     additional_images= forms.ImageField(
        
#         required=False
#     )
#     class Meta:
#         model= Testimonial
#         fields=['name','email','text','image', 'permission']
#         widgets={
#             'additional_images': forms.ClearableFileInput(attrs={'allow_multiple_selected':True}),
            
#         }


class TestimonialForm(forms.ModelForm):
    additional_images = forms.FileField(
        # widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = Testimonial
        widgets={
            'additional_images': forms.ClearableFileInput(attrs={'allow_multiple_selected':True}),
            
        }
        fields = ['name', 'space', 'email', 'text', 'image', 'permission', 'additional_images']
