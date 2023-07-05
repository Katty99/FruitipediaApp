from django.core.exceptions import ValidationError


def contains_only_letters(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Fruit name should contain only letters!")