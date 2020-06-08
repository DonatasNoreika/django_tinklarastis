from .models import Komentaras
from django import forms

class KomentarasForm(forms.ModelForm):
    class Meta:
        model = Komentaras
        fields = ('straipsnis_id', 'komentatorius', 'vardas', 'el_pastas', 'komentaras')
        widgets = {'straipsnis_id': forms.HiddenInput(), 'komentatorius': forms.HiddenInput()}