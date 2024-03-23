from django.urls import path
from . import views
appname = 'GestionInscriptions'



urlpatterns = [
    path('', views.accueil, name='accueil'),
]

