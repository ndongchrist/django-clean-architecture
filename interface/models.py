from django.db import models

# Create your models here.
class CarModel(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    speed = models.FloatField()