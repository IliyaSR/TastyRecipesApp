from django.shortcuts import render, redirect

from TastyRecipesApp.profiles.models import Profile
from TastyRecipesApp.recipes.forms import RecipeForm, RecipeDeleteForm
from TastyRecipesApp.recipes.models import Recipe


def get_profile():
    return Profile.objects.first()


# Create your views here.
def home(request):
    profile = get_profile()

    return render(request, template_name='home-page.html', context={'profile': profile})


def catalogue(request):
    recipes = Recipe.objects.all()
    profile = get_profile()
    context = {
        'recipes': recipes,
        'profile': profile
    }
    return render(request, template_name='catalogue.html', context=context)


def recipe_create(request):
    profile = get_profile()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            return render(request, template_name='create-recipe.html', context={'form': form, 'profile': profile})
    form = RecipeForm()
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, template_name='create-recipe.html', context=context)


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    profile = get_profile()
    recipe.ingredients = recipe.ingredients.split(", ")
    context = {
        'recipe': recipe,
        'profile': profile
    }
    return render(request, template_name='details-recipe.html', context=context)


def recipe_edit(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    profile = get_profile()
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        return render(request, template_name='edit-recipe.html', context={'form': form, 'profile': profile})
    form = RecipeForm(instance=recipe)
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, template_name='edit-recipe.html', context=context)


def recipe_delete(request, recipe_id):
    profile = get_profile()
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe.delete()
            return redirect('catalogue')
    form = RecipeDeleteForm(instance=recipe)
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, template_name='delete-recipe.html', context=context)
