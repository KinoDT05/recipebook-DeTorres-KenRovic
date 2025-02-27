from django.contrib import admin
from .models import Ingredients, Recipe, RecipeIngredient
# Register your models here.


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine,]

admin.site.register(Recipe, RecipeAdmin)
