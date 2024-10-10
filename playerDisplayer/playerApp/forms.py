from django import forms
from .models import Default
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DefaultForm(forms.ModelForm):
    class Meta:
        model = Default
        fields = ['name', 'fire', 'water', 'ground', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 300px;'}),
            'fire': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 4, 'style': 'width: 300px;'}),
            'water': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 4, 'style': 'width: 300px;'}),
            'ground': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 4, 'style': 'width: 300px;'}),
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 40}), 
        }

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1']