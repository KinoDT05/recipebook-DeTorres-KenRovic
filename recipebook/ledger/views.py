from email.mime import image
from django.shortcuts import render, redirect
from .models import Ingredients, Recipe, RecipeIngredient, RecipeImage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .forms import RecipeForm

def index(request):
    return HttpResponse('Hello World! This came from the index view')


class recipe_list(ListView):
    model = Recipe
    template_name = 'list.html'


class recipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe.html'

def createRecipe(request):
    form = RecipeForm()
    notice =""

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        
        if form.is_valid():
            r = Recipe()
            recipeImage = RecipeImage()
            r.name = form.cleaned_data.get('name')
            r.author = form.cleaned_data.get('author')
            recipeImage.image = form.cleaned_data.get('recipeImage')
            recipeImage.description = form.cleaned_data.get('imageDescription')
            r.save()
            recipeImage.recipe = r
            recipeImage.save()

            return redirect('/recipe/list')
        else:
            notice = "Wrong Input"
    ctx = {
            'notice': notice,
            'recipeForm': form
            }    

    return render(request, 'recipe_form.html',ctx)