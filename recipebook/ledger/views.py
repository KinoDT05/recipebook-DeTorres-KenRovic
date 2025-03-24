from email.mime import image
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Ingredients, Recipe, RecipeIngredient, RecipeImage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .forms import RecipeForm, RecipeImageForm

def index(request):
    return HttpResponse('Hello World! This came from the index view')


class recipe_list(ListView):
    model = Recipe
    template_name = 'list.html'


class recipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe.html'
   
    def post(self, request, *args, **kwargs):
        recipe = self.get_object()
        return redirect(reverse("ledger:recipeImageAdd",args=[str(self.pk)]))

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

def addRecipeImage(request,pk):
    form = RecipeImageForm()
    notice =""

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        r = Recipe.objects.get(pk=pk)
        if form.is_valid():
            recipeImage = RecipeImage()
            recipeImage.image = form.cleaned_data.get('recipeImage')
            recipeImage.description = form.cleaned_data.get('imageDescription')
            recipeImage.recipe = r
            recipeImage.save()

            return redirect(r.get_absolute_url())
        else:
            notice = "Wrong Input"
    ctx = {
            'notice': notice,
            'recipeForm': form
            }    

    return render(request, 'recipe_form.html',ctx)