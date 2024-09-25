from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('livres/', views.liste_livres, name='liste_livres')
]