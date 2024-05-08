from django.core.validators import MinLengthValidator
from django.db import models

from TastyRecipesApp.profiles.validators import validator_about_first_capital_letter


# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(max_length=20,
                                validators=(MinLengthValidator(2, message="Nickname must be at least 2 chars long!"),))
    first_name = models.CharField(max_length=30, validators=(validator_about_first_capital_letter,))
    last_name = models.CharField(max_length=30, validators=(validator_about_first_capital_letter,))
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
