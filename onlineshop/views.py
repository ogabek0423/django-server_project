
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from products.models import Product, Category, Bestsellers, FeaturedItems
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.forms import UserRegisterForm, UserLoginForm


class IndexView(View):
    def get(self, request):
        featured_products = FeaturedItems.objects.all()
        category = Category.objects.all()

        search = request.GET.get('search')
        if not search:
            products = Product.objects.all()

            context = {
                'products': products,
                'freshs': featured_products,
                'category': category,
                'bestsellers': Bestsellers.objects.all(),
            }
        else:
            products = Product.objects.filter(name__icontains=search)
            if not products:
                return redirect('404')
            else:
                context = {
                    'products': products,
                    'freshs': featured_products,
                    'category': category,
                    'bestsellers': Bestsellers.objects.all(),
                }

                return render(request, 'index.html',  context)

        products = Product.objects.all()
        context = {
            'products': products,
            'freshs': featured_products,
            'category': category,
            'bestsellers': Bestsellers.objects.all(),
        }
        return render(request, 'index.html', context)

    def post(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

