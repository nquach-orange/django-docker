from django.contrib import admin
from .models import Livre, Etudiant, Categorie, Emprunt

# Register your models here.

admin.site.register(Livre)

admin.site.register(Categorie)