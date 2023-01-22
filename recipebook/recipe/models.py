from django.db import models

# Create your models here.
class Recipe(models.Model):
    dish_name = models.TextField()
    prep_time = models.TextField()
    cook_time = models.TextField
    ingredients = models.TextField()
    steps = models.TextField()