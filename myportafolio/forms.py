from django import forms
from django.forms import ModelForm
from .models import PortafolioModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class loginform(forms.Form):
    Usuarioo = forms.CharField(max_length=50)
    Contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput, strip=False)



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]




class PortafolioForm(ModelForm):
    titulo = forms.CharField(min_length=3, max_length=20)
    class Meta:
        model = PortafolioModel
        fields = ['titulo', 'foto', 'descripcion', 'url', 'tags']

