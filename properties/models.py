from django.db import models
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
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="photos"
    )
    photos = models.ImageField(upload_to=path_and_rename, max_length=255)

    def __str__(self) -> str:
        return "%s" % (self.property.title)
