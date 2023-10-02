from rest_framework import serializers
from .models import Property, PropertyImage

class PropertyImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = "__all__"

class PropertySerializer(serializers.ModelSerializer):
    photos = PropertyImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    owner_username = serializers.CharField(source='owner.username', required=False)

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        property = Property.objects.create(**validated_data)

        for image in uploaded_images:
            PropertyImage.objects.create(property=property, photos=image)

        return property

    class Meta:
        model = Property
        fields = '__all__'
        