from django.urls import path
from .views import index, recipe_list,  recipeDetail, createRecipe, addRecipeImage



urlpatterns = [
	path('', index, name='index'),
	path('recipe/add', createRecipe, name='add'),
	path('recipe/list', recipe_list.as_view(), name='list'),
	path('recipe/<int:pk>', recipeDetail.as_view(), name='recipe'),
	path('recipe/<int:pk>/add', addRecipeImage, name='recipeImageAdd'),
]



app_name = "ledger"