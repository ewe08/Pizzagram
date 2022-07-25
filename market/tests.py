from django.test import TestCase
from .models import *


class PizzaModelTests(TestCase):
    def price_pizza_is_sum_prices_toppings(self):
        """
        The price of pizza is the sum of the prices of toppings
        """
        pizza = Pizza()
