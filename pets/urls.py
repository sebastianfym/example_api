from django.urls import path
from .views import ListPets, PetEdit

urlpatterns = [
    path('', ListPets.as_view(), name='api_list'),
    path('edit/<int:pk>/', PetEdit.as_view(), name='api_detail'),
]