from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Recipe(models.Model):
    CUISINE_TYPE = (
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other')
    )

    title = models.CharField(max_length=100, validators=(MinLengthValidator(10),))
    cuisine_type = models.CharField(max_length=7, choices=CUISINE_TYPE)
    ingredients = models.TextField(help_text='Ingredients must be seperated by a comma and space.')
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(validators=(MinValueValidator(1),),
                                              help_text='Provide the cooking time in minutes.')
    image_url = models.URLField(blank=True, null=True)