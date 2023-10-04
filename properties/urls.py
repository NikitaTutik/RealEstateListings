from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PropertyListCreateView, PropertyRetrieveUpdateDeleteView

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDeleteView.as_view(), name='property-detail'),
]