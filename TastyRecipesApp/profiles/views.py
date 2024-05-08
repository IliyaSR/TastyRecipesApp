from django.shortcuts import render, redirect

from TastyRecipesApp.profiles.forms import ProfileForm, ProfileEditForm, ProfileDeleteForm
from TastyRecipesApp.recipes.models import Recipe
from TastyRecipesApp.recipes.views import get_profile


# Create your views here.
def profile_create(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            return render(request, template_name='create-profile.html', context={'profile': profile, 'form': form})
    form = ProfileForm()
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, template_name='create-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    publishes = Recipe.objects.all()
    context = {
        'profile': profile,
        'publishes': publishes
    }
    return render(request, template_name='details-profile.html', context=context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
        else:
            return render(request, template_name='edit-profile.html', context={'form': form, 'profile': profile})
    form = ProfileEditForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, template_name='edit-profile.html', context=context)


def profile_delete(request):
    profile = get_profile()
    recipes = Recipe.objects.all()
    if request.method == 'POST':
        profile.delete()
        recipes.delete()
        return redirect('home')

    context = {
        'profile': profile
    }

    return render(request, template_name='delete-profile.html', context=context)
