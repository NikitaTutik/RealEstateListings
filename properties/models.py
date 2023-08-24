from django.db import models
from users.models import CustomUser 

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    sqft = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='properties/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title