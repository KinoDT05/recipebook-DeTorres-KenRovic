from django.urls import path
from .views import index, recipe_list,  recipeDetail

urlpatterns = [
	path('', index, name='index'),
	path('recipe/list', recipe_list.as_view(), name='list'),
	path('recipe/<int:pk>', recipeDetail.as_view(), name='recipe'),
]
app_name = "ledger"