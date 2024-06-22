from django_filters import rest_framework as filters
from .models import Ingredients

class IngredientsFilter(filters.FilterSet):
    recipe = filters.CharFilter(lookup_expr='in')
    class Meta:
        model = Ingredients
        fields = ['recipe']