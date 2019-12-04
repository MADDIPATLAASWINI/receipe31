from django.forms import ModelForm
from .models import Receipe
from django import forms

class ReceipeForm(ModelForm):
    class Meta:
        model=Receipe
        fields=['receipe_name','ingredients','process']

