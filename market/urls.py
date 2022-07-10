from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.PizzaListView.as_view(), name='pizza_list'),
    path('new/', views.PizzaCreateView.as_view(), name='pizza_new'),
    path('<int:pk>/', views.PizzaDetailView.as_view(), name='pizza_detail'),
    # path('<int:pk>/edit/', views.PizzaUpdateView.as_view(), name='pizza_update'),
    path('<int:pk>/delete/', views.PizzaDeleteView.as_view(), name='pizza_delete')
]
