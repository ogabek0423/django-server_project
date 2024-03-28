from django.contrib import admin
from django.urls import path, include
from .views import ShopView, ShopDetailView, NotFound, CartView


urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('detail/', ShopDetailView.as_view(), name='detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('404/', NotFound.as_view(), name='404'),

]

