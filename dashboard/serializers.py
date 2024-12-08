from rest_framework import serializers
from .models import Space

class SpaceSerializer(serializers.ModelSerializer):
    questions = serializers.ListField(
        child=serializers.CharField(max_length=255),
        help_text="List of questions (up to 5 or more).",
    )
    extra_information = serializers.JSONField(
        required=False, help_text="Additional fields like name, email, etc."
    )

    class Meta:
        model = Space
        fields = [
            
            "name",
            "logo",
            "header_title",
            "custom_message",
            "questions",
            "extra_information",
            "collection_type",
            "star_ratings_enabled",
            "theme",
            "button_color",
            "language",
            "auto_translate",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [ "created_at", "updated_at"]