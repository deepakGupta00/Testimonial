from django.db import models
from dashboard.models import Space
# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    space= models.ForeignKey( Space,related_name='testimonial' , on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/images/', blank=True, null=True)
    additional_images = models.ManyToManyField('TestimonialImage', blank=True)
    permission = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial by {self.name}"

class TestimonialImage(models.Model):
    image = models.ImageField(upload_to='testimonials/additional_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"