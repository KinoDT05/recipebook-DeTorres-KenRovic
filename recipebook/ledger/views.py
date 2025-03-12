from django.shortcuts import render
from .models import Ingredients, Recipe, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! This came from the index view')


class recipe_list(ListView):
    model = Recipe
    template_name = 'list.html'


class recipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe.html'
