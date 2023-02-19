from django import forms
from .models import Car


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make','year','photo', 'url')