from django import  forms
from .models import Shop,Review

class ShopForm(forms.ModelForm):

    class Meta:
        model   = Shop
        fields  = [ "name","lat","lon" ]

class ReviewForm(forms.ModelForm):

    class Meta:
        model   = Review
        fields  = [ "shop","comment","ip","image","star" ]
