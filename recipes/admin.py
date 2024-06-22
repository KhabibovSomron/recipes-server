from django.contrib import admin
from .models import Recipes, Ingredients

# Register your models here.

admin.site.site_header = "Recipes Administration"

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cooking_time']

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'quintity']
