from django import forms

from .models import SeialNumber

class SeialnumberModelForm(forms.ModelForm):
    class Meta:
        model = SeialNumber
        fields = [
            'running_number'
        ]