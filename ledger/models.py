from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Recipe(models.Model):
    name = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=str(self.pk))


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absoulute_url(self):
        return reverse("ledger:ingredient_detail", args=str(self.pk))


class RecipeIngredient(models.Model):
    quantity = models.FloatField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} in {self.recipe.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(
        validators=[
            MinLengthValidator(255, "Bio must be at least 255 characters long.")
        ]
    )
