from django import forms
from rango.models import Category,Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category._meta.get_field('name').max_length, help_text="Please enter the category name:")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)
    
    #An inline class to provide addiitional information on the form. Very useful!
    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page._meta.get_field('title').max_length, help_text = "Pease enter the title of the page:")
    url = forms.URLField(max_length=Page._meta.get_field('url').max_length, help_text="Please enter the URL of the page:")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Page
        exclude = ('category',)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('get')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data