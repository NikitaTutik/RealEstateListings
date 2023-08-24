from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDeleteView,  CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]