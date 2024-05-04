from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant
from .forms import Etudiant_forms
from django.http import HttpResponse
# Create your views here.

def etudiants (request):
    etudiants=Etudiant.objects.all
    return render (request, 'inscription.html', {'etudiants':etudiants})

def index (request):
    return render(request,'index.html')

def details_etudiants(request,id):
    etudiant= Etudiant.objects.get(id=id)
    return render(request,'details_etudiants.html',{'etudiant':etudiant})

def ajouter_etudiant (request):
    form = Etudiant_forms()
    if request.method == 'POST':
        form = Etudiant_forms(request.POST)
        form.save()  #enregistrer dans la base de données
    return render(request,'forms.html',{'form':form})
def update_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, pk=id)
    if request.method == 'POST':
        form = Etudiant_forms(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('accueil')  # Redirige vers la page d'accueil après la mise à jour
    else:
        form = Etudiant_forms(instance=etudiant)
    return render(request, 'update_etudiant.html', {'form': form})
    return render(request,'forms.html',{'form':form})
def delete_etudiant(request, id):
    if request.method == 'POST':
        etudiant = Etudiant.objects.get(pk=id)
        etudiant.delete()
        return redirect('accueil')  # Redirige vers la page d'accueil après la suppression
    else:
        return HttpResponse("Méthode non autorisée")  # Réponse HTTP pour les méthodes autres que POST