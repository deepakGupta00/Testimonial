from rest_framework import serializers
from dashboard.models import Space

class SpaceSerializers(serializers.ModelSerializer):
    class Meta:
        model= Space
        fields="__all__"