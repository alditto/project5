from django.shortcuts import render
from rest_framework import viewsets
from .models import Autor, Editorial, Libro
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer
from rest_framework.response import Response
from .views import views

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class BuscarLibrosAPIView(views.APIView):
    def get(self, request, format=None):
        titulo = request.GET.get('titulo', '')
        libros = Libro.objects.filter(titulo__icontains=titulo)
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)
