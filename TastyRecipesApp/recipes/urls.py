from django.urls import path, include

from TastyRecipesApp.recipes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/catalogue/', views.catalogue, name='catalogue'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:recipe_id>/', include([
        path('details/', views.recipe_details, name='recipe_details'),
        path('edit/', views.recipe_edit, name='recipe_edit'),
        path('delete/', views.recipe_delete, name='recipe_delete')
    ]))
]
