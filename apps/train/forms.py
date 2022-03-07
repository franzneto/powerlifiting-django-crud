from django import forms
from .models import Train

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['exercise','weight', 'repetitions', 'date']