from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from .models import Livre, Categorie, Auteur, Emprunt, Personnel, Appartient
from .serializers import LivreSerializer, CategorieSerializer, AuteurSerializer, EmpruntSerializer, AppartientSerializer, PersonnelSerializer, AppartientSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class LivreList(generics.ListCreateAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

class LivreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    lookup_field = 'id_livre'

class AuteurList(generics.ListCreateAPIView):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

class AuteurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    lookup_field = 'id_auteur'


class CategorieList(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    lookup_field = 'id_categorie'

class EmpruntList(generics.ListCreateAPIView):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

class EmpruntDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    lookup_field = ('id_eleve', 'id_livre', 'id_personnel')


class PersonnelList(generics.ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class PersonnelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    lookup_field = 'id_personnel'


class AppartientList(generics.ListCreateAPIView):
    queryset = Appartient.objects.all()
    serializer_class = AppartientSerializer

class AppartientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appartient.objects.all()
    serializer_class = AppartientSerializer
    lookup_field = ('id_categorie', 'id_livre')