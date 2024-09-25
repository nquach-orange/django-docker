from django.shortcuts import render
from django.http import HttpResponse
from .models import Livre

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def liste_livres(request):
    livres = Livre.objects.all()  # Récupère tous les livres de la base de données
    return render(request, 'liste_livres.html', {'livres': livres})