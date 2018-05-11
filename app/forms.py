from django import forms

class UploadImageForm(forms.Form):
    file_field = forms.FileField()