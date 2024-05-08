from django import forms

from TastyRecipesApp.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('__all__')
        widgets = {
            'ingredients': forms.Textarea(attrs={
                'help_text': 'Ingredients must be seperated by a comma and space.',
                'placeholder': "ingredient1, ingredient2, ..."
            }),
            'instructions': forms.Textarea(attrs={
                'placeholder': 'Enter detailed instructions here...'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Optional image URL here...'
            })
        }


class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(RecipeDeleteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # if field_name == 'cuisine_type':
            # field.widget.attrs['disabled'] = 'disabled'
            # else:
            # field.widget.attrs['readonly'] = 'readonly'
