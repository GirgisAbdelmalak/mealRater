from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def __str__(self):
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(to=Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # def __str__(self):
    #     return self.meal
    
    class meta:
        unique_together = (('user','meal'),)
        index_together = (('user','meal'),)