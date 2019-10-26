from django import forms
from .models import Page
from django.contrib.auth.models import User


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'avatar', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '', 'content': '', 'created_by': '', 'avatar': '',
        }
