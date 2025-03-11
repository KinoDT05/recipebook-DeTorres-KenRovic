from django.db import models
from django.urls import reverse


class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient', args=[self.pk])

class Recipe(models.Model): 
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    
    