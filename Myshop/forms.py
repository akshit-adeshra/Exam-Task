from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


