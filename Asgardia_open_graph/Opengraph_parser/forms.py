from django import forms

class URLForm(forms.Form):
    url_field = forms.URLField()