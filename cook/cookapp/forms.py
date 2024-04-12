from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'video_link', 'method', 'prep_time', 'ingredients', 'image', 'cuisine']

# class CuresForm(forms.ModelForm):
#     class Meta:
#         model = Cures
#         fields = ['age', 'weight', 'height', 'country', 'disease', 'allergies', 'state', 'city']