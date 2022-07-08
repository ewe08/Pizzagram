from django.contrib.auth.models import User
from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    toppings = models.ManyToManyField(Topping)


class Product(models.Model):
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
