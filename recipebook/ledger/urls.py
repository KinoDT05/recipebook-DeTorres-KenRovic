from django.urls import path
from .views import index, recipe_list,  recipeDetail

urlpatterns = [
	path('', index, name='index'),
	path('recipe/list', recipe_list, name='list'),
	path('recipe/<int:id>', recipeDetail, name='recipe'),
]
app_name = "ledger"