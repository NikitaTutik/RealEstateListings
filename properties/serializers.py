from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', required=False)
    class Meta:
        model = Property
        fields = '__all__'