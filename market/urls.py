from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.PizzaListView.as_view(), name='pizza_list'),
    path('pizza/new/', views.PizzaCreateView.as_view(), name='pizza_new'),
    path('pizza/<int:pk>/', views.PizzaDetailView.as_view(), name='pizza_detail')
]
