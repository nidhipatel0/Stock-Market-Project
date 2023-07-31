from django import forms
from .models import Photo, Stock


class PhotoForm(forms.ModelForm):
    # photo = forms.ImageField(
    #     label = "Photo",
    #     widget=forms.ClearableFileInput(attrs={"mutiple":True}),
    # )

    class Meta:
        
        model = Photo
        fields = ["comment","stock",'portfolio_category']



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