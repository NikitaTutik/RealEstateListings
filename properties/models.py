from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from users.models import CustomUser
from .helpers import path_and_rename


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    sqft = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    def validate_image(image):
        file_size = image.file.size
        limit_mb = 2
        if file_size > limit_mb * 1024 * 1024:
            raise ValidationError("Max size of an image is %s MB" % limit_mb)

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="photos"
    )
    photos = models.ImageField(
        upload_to=path_and_rename,
        validators=[
            FileExtensionValidator(allowed_extensions=["png", "jpeg", "jpg"]),
            validate_image,
        ],
        max_length=255,
    )

    def __str__(self) -> str:
        return "%s" % (self.property.title)
