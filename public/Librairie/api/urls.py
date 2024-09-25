from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('livres/', LivreList.as_view(), name='livre-list'),
    path('livres/<int:id_livre>/', LivreDetail.as_view(), name='livre-detail'),
    path('auteurs/', AuteurList.as_view(), name='auteur-list'),
    path('auteurs/<int:id_auteur>/', AuteurDetail.as_view(), name='auteur-detail'),
    path('categories/', CategorieList.as_view(), name='categorie-list'),
    path('categories/<int:id_categorie>/', CategorieDetail.as_view(), name='categorie-detail'),
    path('emprunts/', EmpruntList.as_view(), name='emprunt-list'),
    path('emprunts/<int:id_eleve>/<int:id_livre>/<int:id_personnel>/', EmpruntDetail.as_view(), name='emprunt-detail'),
    path('personnels/', PersonnelList.as_view(), name='personnel-list'),
    path('personnels/<int:id_personnel>/', PersonnelDetail.as_view(), name='personnel-detail'),
]
