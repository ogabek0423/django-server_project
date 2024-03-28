from django.shortcuts import render
from .models import Product, Category, Bestsellers, FeaturedItems
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'products/shop.html')


class ShopDetailView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'products/shop-detail.html')


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'products/cart.html')


class NotFound(View):
    def get(self, request):
        return render(request, 'products/404.html')

