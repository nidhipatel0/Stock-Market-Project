from django import forms
from .models import Photo


# class PhotoForm(forms.ModelForm):
#     # photo = forms.ImageField(
#     #     label = "Photo",
#     #     widget=forms.ClearableFileInput(attrs={"mutiple":True}),
#     # )
#     #i = Photo._meta.pk.name
#     class Meta:
#         i = Photo._meta.pk.name
#         model = Photo
#         fields = [Photo.photo]



# class MultipleFileInput(forms.FileInput):
#     def __init__(self, attrs=None):
#         attrs = attrs or {}
#         attrs['multiple'] = True
#         super().__init__(attrs=attrs)

# class PhotoForm(forms.ModelForm):
#     photo = forms.ImageField(
#         label = "Photo",
#         widget = forms.ClearableFileInput(attrs = {"multiple":True}),
#     )
#     class Meta:
#         model = Photo
#         fields = ['photo', 'comment','stock']
# class StockForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields= [
#             'name'
#         ]

# all = Stock.objects.all()
# pk = []
# for b in all:
#     pk.append(b)        