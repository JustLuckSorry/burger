from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product, Order, OrderItem


class HomeView(TemplateView):
    template_name = 'shop/index.html'


class MenuView(TemplateView):
    template_name = 'shop/Menu.html'


class BlogView(TemplateView):
    template_name = 'shop/blog.html'


class AboutView(TemplateView):
    template_name = 'shop/about.html'


class ContactView(TemplateView):
    template_name = 'shop/contact.html'


class ProductListView(ListView):
    template_name = 'shop/Menu.html'
    model = Product
    paginate_by = 12


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shop/Menu-element.html'
    model = Product
    login_url = '/login/'
