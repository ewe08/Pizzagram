from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.MarketView.as_view(), name='pizza_list'),
]
