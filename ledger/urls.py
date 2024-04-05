from django.urls import path

from .views import RecipeDetailView, RecipeListView, RecipeCreateView, ImageCreateView


urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path("recipe/add", RecipeCreateView.as_view(), name="recipe_create"),
    path(
        "recipe/<int:pk>/add_image",
        ImageCreateView.as_view(),
        name="recipe_add_image",
    ),
]

app_name = 'ledger'
