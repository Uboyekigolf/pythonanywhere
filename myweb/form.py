from django.forms import ModelForm
from django import forms

from .models import herb




class SearchForm(forms.Form):

    keyword = forms.CharField(max_length=100)