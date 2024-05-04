from django.contrib import admin

# Register your models here.
from .models import Etudiant, Annees,  Inscrits

admin.site.register(Etudiant)
admin.site.register(Annees)
admin.site.register(Inscrits)