from django.urls import path
from .views import RecipeCreateAPIView, RecipeUpdateAPIView, RecipeDestroyAPIView, RecipeListAPIView, IngredientCreateAPIView, IngredientDestroyAPIView, IngredientListAPIView, IngredientUpdateAPIView, RecipeRetrieveAPIView, RecipeImageUpdateAPIView

urlpatterns = [
    path('add-recipe/', RecipeCreateAPIView.as_view(), name='add-recipe'),
    path('update-recipe/<int:pk>/', RecipeUpdateAPIView.as_view(), name='update-recipe'),
    path('update-recipe-image/<int:pk>/', RecipeImageUpdateAPIView.as_view(), name='update-recipe-image'),
    path('destroy-recipe/<int:pk>/', RecipeDestroyAPIView.as_view(), name='destroy-recipe'),
    path('recipes/', RecipeListAPIView.as_view(), name='recipes'),
    path('recipe/<int:pk>/', RecipeRetrieveAPIView.as_view(), name='recipe'),

    path('add-ingredient/', IngredientCreateAPIView.as_view(), name='add-ingredient'),
    path('update-ingredient/<int:pk>/', IngredientUpdateAPIView.as_view(), name='update-ingredient'),
    path('destroy-ingredient/<int:pk>/', IngredientDestroyAPIView.as_view(), name='destroy-ingredient'),
    path('ingredients/', IngredientListAPIView.as_view(), name='ingredients'),
]
