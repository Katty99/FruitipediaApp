from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruit.validators import contains_only_letters


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2), contains_only_letters])
    image = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(blank=True, null=True)
