from django import forms

from .models import *


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        exclude = ["author"]


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = "__all__"
        exclude = ["recipe"]