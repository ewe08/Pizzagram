from django.http import request
from django.shortcuts import redirect
from django.views import generic

from .models import Pizza, Product


class PizzaListView(generic.ListView):
    model = Product
    template_name = 'market/market.html'
    context_object_name = 'pizza_list'

    def get_queryset(self):
        return Product.objects.all()


class PizzaDetailView(generic.DetailView):
    model = Pizza
    template_name = 'market/post_detail.html'


class PizzaCreateView(generic.CreateView):
    model = Pizza
    template_name = 'market/post_new.html'
    fields = ['name', 'size', 'side', 'dough', 'cheese', 'sauce', 'meat', 'vegetable']

    def form_valid(self, form):
        pizza = form.save(commit=False)
        pizza.price = pizza.size.price + pizza.side.price + pizza.dough.price
        # pizza.cheese.through.objects.all()
        pizza.save()

        prod = Product()
        prod.pizza = pizza
        prod.creator = self.request.user
        prod.save()

        return redirect('market:pizza_list')
