from rest_framework import generics
from .models import CustomUser
from .serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = CustomUser.objects.get(username=request.data['username'])
        response.data['user_id'] = user.id
        return response