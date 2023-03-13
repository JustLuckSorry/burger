from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    template_name = 'shop/Menu.html'
    model = Product
    paginate_by = 12

