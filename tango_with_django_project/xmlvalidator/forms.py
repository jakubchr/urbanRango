from django import forms
from xmlvalidator.models import XMLDocument

class XMLForm(forms.ModelForm):
    class Meta:
        model = XMLDocument
        fields = ('description', 'xml', )
