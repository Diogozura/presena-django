from django import forms
from .models import Reuniao

class ReuniaoForm(forms.ModelForm):

    class Meta:
        model = Reuniao
        fields = ['id', 'ausente']

