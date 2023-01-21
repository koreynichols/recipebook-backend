from django.db import models

# Create your models here.
class Recipe(models.Model):
    dish = models.TextField()
    ingredients = models.TextField()