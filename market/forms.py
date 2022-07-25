from django import forms
from django.shortcuts import get_object_or_404

from .models import *


# class CreateForm(forms.Form):
#     sizes = (
#         (get_object_or_404(Size, name="Маленькая(20 см)").pk, 'Маленькая(20 см)'),
#         (get_object_or_404(Size, name='Средняя(30 см)').pk, 'Средняя(30 см)'),
#         (get_object_or_404(Size, name='Большая(40 см)').pk, 'Большая(40 см)'),)
#
#     doughs = (
#         (get_object_or_404(Dough, name="Тонкое тесто").pk, 'Тонкое тесто'),
#         (get_object_or_404(Dough, name="Традиционное тесто").pk, 'Традиционное тесто'),)
#
#     sides = (
#         (get_object_or_404(Side, name="Сырный бортик").pk, 'Сырный бортик'),
#         (get_object_or_404(Side, name="Мясной бортик").pk, 'Мясной бортик'),
#         (get_object_or_404(Side, name="Обычный бортик").pk, 'Обычный бортик'),)
#
#     pizza_name = forms.CharField(label='Название пиццы', max_length=100)
#     pizza_size = forms.ChoiceField(choices=sizes, widget=forms.RadioSelect)
#     pizza_side = forms.ChoiceField(choices=sides, widget=forms.RadioSelect)
#     pizza_dough = forms.ChoiceField(choices=doughs, widget=forms.RadioSelect)
#
#     pizza_cheeses = forms.ModelMultipleChoiceField(
#         queryset=Cheese.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True)
#     pizza_meats = forms.ModelMultipleChoiceField(
#         queryset=Meat.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True)
#     pizza_vegetables = forms.ModelMultipleChoiceField(
#         queryset=Vegetable.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True)
#     pizza_sauces = forms.ModelMultipleChoiceField(
#         queryset=Sauce.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True)
#
#     class Meta:
#         model = Pizza
#         fields = ['__all__']
#         widgets = {
#             'size': forms.RadioSelect()
#         }
