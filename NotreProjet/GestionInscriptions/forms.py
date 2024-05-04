from django import forms
from .models import Etudiant

class Etudiant_forms(forms.ModelForm):

    class Meta:

        model= Etudiant
        fields= "__all__"

