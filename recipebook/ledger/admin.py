from django.contrib import admin
from .models import Ingredients, Recipe, RecipeIngredient, RecipeImage
# Register your models here.


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        RecipeIngredientInLine,
        RecipeImageInline,
        ]

admin.site.register(Recipe, RecipeAdmin)
