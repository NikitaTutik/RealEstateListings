from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_permissions(self):
        method = self.request.method
        if method == "POST":
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

class PropertyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
