from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Topping(models.Model):
    name = models.CharField(max_length=70)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Cheese(Topping):
    pass


class Sauce(Topping):
    pass


class Meat(Topping):
    pass


class Size(Topping):
    pass


class Dough(Topping):
    pass


class Side(Topping):
    pass


class Vegetable(Topping):
    pass


class Pizza(models.Model):
    name = models.CharField(max_length=50)

    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    side = models.ForeignKey(Side, on_delete=models.CASCADE)
    dough = models.ForeignKey(Dough, on_delete=models.CASCADE)

    cheese = models.ManyToManyField(Cheese)
    meat = models.ManyToManyField(Meat)
    sauce = models.ManyToManyField(Sauce)
    vegetable = models.ManyToManyField(Vegetable)

    price = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('market:pizza_list')

    def __str__(self):
        return self.name


class Product(models.Model):
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
    creator = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
