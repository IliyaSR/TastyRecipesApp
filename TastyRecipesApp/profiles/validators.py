from django.core.exceptions import ValidationError


def validator_about_first_capital_letter(word):
    if not word[0].isupper():
        raise ValidationError("Name must start with a capital letter!")
