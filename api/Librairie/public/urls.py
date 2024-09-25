# public/urls.py
from django.urls import path
from .views import home, livres, categories, auteurs

urlpatterns = [
    path('', home, name='home'),
    path('livres/', livres, name='livres'),
    path('categories/', categories, name='categories'),
    path('auteurs/', auteurs, name='auteurs'),
]