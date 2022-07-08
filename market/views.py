from django.shortcuts import render
from django.views import generic

from .models import User


class MarketView(generic.ListView):
    template_name = 'market/market.html'
    context_object_name = 'latest_pizza_list'

    def get_queryset(self):
        return User.objects.all()
