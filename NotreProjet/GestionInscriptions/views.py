from django.shortcuts import render
from . import views
appname = 'GestionInscriptions'

def accueil(request):
    return render(request, 'index.html')
