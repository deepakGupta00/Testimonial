from django.db import models
    
from uuid import uuid4
from django.utils.text import slugify

class Space(models.Model):
    
    
    id=models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name=models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    logo=models.ImageField(upload_to="space_logos/" ,blank=True)
    header_title=models.CharField(max_length=255)
    custom_message=models.TextField()
    questions= models.TextField(help_text="Add up to 5 questions separated by new lines")
    extra_information=models.JSONField(default=dict, blank=True)
    collection_type= models.CharField(max_length=10 , choices=[("text","Text"),("video","Video"),("both", "Text and Video")], default="text")
    
    star_ratings_enabled = models.BooleanField(default=False)
    theme = models.CharField(max_length=50, default="default")
    button_color = models.CharField(max_length=7, default="#000000")  
    language = models.CharField(max_length=50, default="English")  
    auto_translate = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class ThankYouPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    space=models.ForeignKey(Space, related_name="thankyoupage", on_delete=models.CASCADE )
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
    

class TestimonialEmailNotification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    space=models.ForeignKey(Space, related_name="testimonialemailnotification", on_delete=models.CASCADE )
    subject_template = models.CharField(
        max_length=255, default="Thank you for your testimonial, {name}!"
    )  
    body_template = models.TextField(
        default=(
            "Hey {name},\n\n"
            "You just made a testimonial to {brand_name} 🥳\n\n"
            "{testimonial_message}\n"
            "Retweet to spread the word 👇\n\n"
            "Share on {social_platform}\n\n"
            "— {sender_name} from {brand_name}\n\n"
            "💗 Love video testimonials? Sign up | Become an affiliate"
        )
    )  
    include_social_share_link = models.BooleanField(default=True)  
    social_share_link_template = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Template for social share link, e.g., https://twitter.com/intent/tweet?text={testimonial_message}",
    ) 
    sender_name = models.CharField(max_length=255, default="Deepak") 
    brand_name = models.CharField(max_length=255, default="Testimonial") 
    affiliate_signup_link = models.URLField(
        max_length=500, blank=True, null=True, help_text="Link for affiliate sign-up"
    )  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Email Notification Template for {self.brand_name}"