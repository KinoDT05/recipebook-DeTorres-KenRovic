from django.contrib import admin
from .models import Ingredients, Recipe, RecipeIngredient
# Register your models here.


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine,]



# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Recipe, RecipeAdmin)
