from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Product


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