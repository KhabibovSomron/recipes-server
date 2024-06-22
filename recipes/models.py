from django.db import models

# Create your models here.

class Recipes(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to='images/')
    cooking_time = models.IntegerField(verbose_name="Время приготовления")


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name="Рецепт")
    title = models.CharField(verbose_name="Название", max_length=255)
    quintity = models.CharField(verbose_name="Объем или количество", max_length=100)

