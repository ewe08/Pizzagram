from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404

# from .forms import CreateForm
from .models import *


class PizzaListView(generic.ListView):
    model = Product
    template_name = 'market/market.html'
    context_object_name = 'pizza_list'

    def get_queryset(self):
        return Product.objects.all()


class PizzaCreateView(generic.CreateView):
    model = Pizza
    template_name = 'market/pizza_new.html'
    fields = ['name', 'size', 'side', 'dough', 'cheese', 'sauce', 'meat', 'vegetable']

    def form_valid(self, form):
        pizza = form.save()
        pizza.set_price_pizza()
        pizza.save()
        prod = Product()
        prod.pizza = pizza
        prod.creator = self.request.user
        prod.save()

        return redirect('market:pizza_list')


class PizzaDetailView(generic.DetailView):
    model = Product
    template_name = 'market/pizza_detail.html'
    context_object_name = 'item'


class PizzaDeleteView(generic.DeleteView):  # Создание нового класса
    model = Product
    template_name = 'market/pizza_delete.html'
    context_object_name = 'item'
    success_url = reverse_lazy('market:pizza_list')

# class PizzaUpdateView(generic.UpdateView):
#     model = Pizza
#     template_name = 'market/pizza_update.html'
#     fields = ['name', 'size', 'side', 'dough', 'cheese', 'sauce', 'meat', 'vegetable']
