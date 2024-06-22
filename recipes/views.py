from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework import status
from .serializers import RecipeSerializer, IngredientSerializer, AddIngredientSerializer, UpdateRecipeSerializer, UpdateRecipeImageSerializer
from .models import Ingredients, Recipes
from .filters import IngredientsFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class RecipeCreateAPIView(CreateAPIView):
    serializer_class = RecipeSerializer


class RecipeUpdateAPIView(UpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = UpdateRecipeSerializer

class RecipeImageUpdateAPIView(UpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = UpdateRecipeImageSerializer        

class RecipeDestroyAPIView(DestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer



class RecipeListAPIView(ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['title', 'description', 'cooking_time']
    ordering_fields = ['title', 'cooking_time']



class IngredientCreateAPIView(CreateAPIView):
    serializer_class = AddIngredientSerializer


class IngredientUpdateAPIView(UpdateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
        

class IngredientDestroyAPIView(DestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer



class IngredientListAPIView(ListAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientsFilter



class RecipeRetrieveAPIView(RetrieveAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer













