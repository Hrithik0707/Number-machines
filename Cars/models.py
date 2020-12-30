from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mpg = models.IntegerField()
    cylinders =models.IntegerField()
    displacement = models.IntegerField()
    horsepower =models.IntegerField()
    weight =models.IntegerField()
    acceleration =models.IntegerField()
    model_year = models.IntegerField()
    origin =models.IntegerField()
    car_name = models.CharField(max_length = 100)

