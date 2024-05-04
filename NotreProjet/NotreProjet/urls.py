"""
URL configuration for GestionAbsences project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path
from GestionInscriptions.views import etudiants, index, details_etudiants, ajouter_etudiant, delete_etudiant, update_etudiant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', etudiants, name='accueil'),
    path('home/', index, name='home'),
    path('details_etudiants/<int:id>/', details_etudiants, name='details_etudiants'),
    path('ajouter_etudiant/', ajouter_etudiant, name='ajouter_etudiant'),
    path('delete_etudiant/<int:id>/', delete_etudiant, name='delete_etudiant'),
    path('update_etudiant/<int:id>/', update_etudiant, name='update_etudiant'),
]
