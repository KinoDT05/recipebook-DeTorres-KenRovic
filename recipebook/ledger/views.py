from django.shortcuts import render
from .models import Ingredients, Recipe, RecipeIngredient
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! This came from the index view')

def recipe_list(request):
    recipes = Recipe.objects.all()

    ctx = {
        'recipes':recipes
    }
    return render(request, "list.html", ctx)

def recipeDetail(request, id):
    recipe = Recipe.objects.get(id=id)
    ingredients = recipe.recipe.all()
    ctx = { 
        'recipe':recipe,
        'ingredients': ingredients
    }

    return render(request, "recipe.html", ctx)

