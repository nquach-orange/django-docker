
from django.contrib import admin
from .models import Livre, Etudiant, Categorie, Emprunt, Auteur, TypeLivre

# Register your models here.

admin.site.register(Livre)
admin.site.register(TypeLivre)
admin.site.register(Auteur)
admin.site.register(Categorie)

