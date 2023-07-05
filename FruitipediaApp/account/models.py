from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.account.validators import name_starts_with_a_letter


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=[MinLengthValidator(2), name_starts_with_a_letter])
    last_name = models.CharField(max_length=35, validators=[MinLengthValidator(1), name_starts_with_a_letter])
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    image_url = models.URLField(blank=True, null=True)
    age = models.CharField(blank=True, null=True, default=18)
