from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import IsAuthenticated

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]  
    
class PropertyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]  