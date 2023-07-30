from django import forms
from .models import Photo

# class MultipleFileInput(forms.FileInput):
#     def __init__(self, attrs=None):
#         attrs = attrs or {}
#         attrs['multiple'] = True
#         super().__init__(attrs=attrs)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'comment','stock']