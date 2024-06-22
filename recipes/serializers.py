from rest_framework import serializers
from .models import Ingredients, Recipes


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'title', 'quintity']

class AddIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'title', 'quintity', 'recipe']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'title', 'description', 'image', 'cooking_time']

class UpdateRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'title', 'description', 'cooking_time']

class UpdateRecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['image',]


