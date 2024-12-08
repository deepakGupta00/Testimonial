from django.db import models
    
from uuid import uuid4

class Space(models.Model):
    choices=[("text","Text"),("video","Video"),("both", "Text and Video")]
    
    id=models.UUIDField(primary_key=True,default=uuid4(), editable=False)
    name=models.CharField(max_length=255)
    logo=models.ImageField(upload_to="space_logos/")
    header_title=models.CharField(max_length=255)
    custom_message=models.TextField()
    questions= models.TextField(help_text="Add up to 5 questions separated by new lines")
    extra_information=models.JSONField(default=dict, blank=True)
    collection_type= models.CharField(max_length=10 , choices=choices, default="text")
    
    star_ratings_enabled = models.BooleanField(default=False)
    theme = models.CharField(max_length=50, default="default")
    button_color = models.CharField(max_length=7, default="#000000")  
    language = models.CharField(max_length=50, default="English")  
    auto_translate = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class ThankYouPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    space=models.ForeignKey(Space, related_name="thankyoupage", )
    thank_you_title = models.CharField(max_length=255)  
    thank_you_message = models.TextField(help_text="Markdown supported") 
    image = models.ImageField(upload_to="thank_you_images/", blank=True, null=True)
    hide_image = models.BooleanField(default=False)  
    allow_social_sharing = models.BooleanField(default=False) 
    redirect_url = models.URLField(
        max_length=500, blank=True, null=True, help_text="Redirect to your own page after submission"
    )  
    reward_for_video = models.BooleanField(
        default=False, help_text="Automatically reward your customer for a video testimonial"
    )  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.thank_you_title