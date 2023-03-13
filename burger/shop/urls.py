from django.urls import path

from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('index/', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact')
    # path('Menu/', ProductListView.as_view(), name='shop_product_list')
]