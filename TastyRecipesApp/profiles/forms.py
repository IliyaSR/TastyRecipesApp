from django import forms

from TastyRecipesApp.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
