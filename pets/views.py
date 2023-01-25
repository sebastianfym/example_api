from django.http import HttpResponseRedirect
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import PetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin


class ListPets(GenericAPIView, ListModelMixin, CreateModelMixin):
    """
    ListPets - представление служащее для  отображения страницы API всех животных. Его url - api/pets/
    """
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class PetEdit(APIView, DestroyModelMixin):
    """
    PetEdit - представление служащее для  отображения страницы API животного по id(pk). Его url - edit/<int:pk>/.
    Где pk - id нужного животного. На этой странице можно удалить животное и изменить данные о нем.
    """
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        obj = Pet.objects.get(id=pk)
        return Response(PetSerializer(obj).data)

    def post(self, request, pk):
        obj = Pet.objects.get(id=pk)
        data = request.data
        obj.name = data.get('name', obj.name)
        obj.age = data.get('age', obj.age)
        obj.date_of_arrival = data.get('date_of_arrival', obj.date_of_arrival)
        obj.weight = data.get('weight', obj.weight)
        obj.height = data.get('height', obj.height)
        obj.special_signs = data.get('special_signs', obj.special_signs)
        obj.save()
        return Response(PetSerializer(obj).data)

    def delete(self, request, pk):
        obj = Pet.objects.get(id=pk)
        obj.delete()
        return HttpResponseRedirect('/api/pets/')


