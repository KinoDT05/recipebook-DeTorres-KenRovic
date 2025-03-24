from django import forms

class RecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=100)
    author = forms.CharField(label='Recipe Authoer', max_length=100)
    recipeImage = forms.ImageField(label = 'Recipe Image')
    imageDescription = forms.CharField(label = 'Image Description',max_length=255)