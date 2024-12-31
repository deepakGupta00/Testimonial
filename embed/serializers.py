from rest_framework import serializers
from feedback.models import Testimonial, TestimonialImage

class TestimonialImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialImage
        fields = ['image']

class TestimonialSerializer(serializers.ModelSerializer):
    additional_images = TestimonialImageSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Testimonial
        fields = [
            'id',
            'name',
            'space',
            'email',
            'text',
            'image',
            'additional_images',
            'permission',
            'created_at',
        ]
        read_only_fields = ['created_at']