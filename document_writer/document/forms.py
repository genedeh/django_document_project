from django import forms
from django.forms import ModelForm

from .models import Document


class DocumentForm(ModelForm):
    doc = forms.CharField(widget=forms.Textarea(attrs={'cols': 189, 'rows': 20}))

    class Meta:
        model = Document
        fields = '__all__'
