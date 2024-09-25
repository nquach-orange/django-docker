from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from api.models import Livre, Emprunt, Categorie, Auteur

def home(request):
    return render(request, 'public/home.html')

def livres(request):
    livres = Livre.objects.all()
    return render(request, 'public/livres.html', {'livres': livres})

def categories(request):
    categories = Categorie.objects.all()
    return render(request, 'public/categories.html', {'categories': categories})

def auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'public/auteurs.html', {'auteurs': auteurs})


