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


cheeses = (
    ('моцарелла', 'Сыр моцарелла'),
    ('реджанито', 'Сыр реджанито'),
    ('чеддер', 'Сыр чеддер'),)


class Cheese(Topping):
    name = models.CharField(max_length=70, choices=cheeses)


sauces = (
    ('традиционный', 'Традиционный соус'),
    ('чесночный', 'Чесночный соус'),
    ('острый', 'Острый соус'),
)


class Sauce(Topping):
    name = models.CharField(max_length=70, choices=sauces)


meats = (
    ('бекон', 'Бекон'),
    ('говядина', 'Говядина'),
    ('Ветчина', 'Ветчина'),)


class Meat(Topping):
    name = models.CharField(max_length=70, choices=meats)


vegetables = (
    ('Шампиньоны', 'Шампиньоны'),
    ('Лук', 'Лук'),
    ('халапеньо', 'Перец халапеньо'),)


class Vegetable(Topping):
    name = models.CharField(max_length=70, choices=vegetables)


class Size(Topping):
    pass


class Dough(Topping):
    pass


class Side(Topping):
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

    def set_price_pizza(self):
        self.price = self.size.price + self.side.price + self.dough.price
        self.save()
        self.price += sum([i.cheese.price for i in self.cheese.through.objects.all()])
        self.price += sum([i.sauce.price for i in self.sauce.through.objects.all()])
        self.price += sum([i.meat.price for i in self.meat.through.objects.all()])
        self.price += sum([i.vegetable.price for i in self.vegetable.through.objects.all()])

    def __str__(self):
        return self.name


class Product(models.Model):
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
    creator = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
