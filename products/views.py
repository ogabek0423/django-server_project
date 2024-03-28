from django.shortcuts import render, redirect
from .models import Product, Category, Bestsellers, FeaturedItems
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Comments


class ShopView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        bestsellers = Bestsellers.objects.all()
        featured = FeaturedItems.objects.all()
        context = {
            'products': products,
            'categories': categories,
            'bestsellers': bestsellers,
            'featured': featured,
        }
        return render(request, 'products/shop.html', context)


class ShopDetailView(LoginRequiredMixin, View):
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
            return render(request, 'products/shop-detail.html', context)
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

                return render(request, 'products/shop-detail.html', context)


        products = Product.objects.all()

        context = {
            'products': products,
            'freshs': featured_products,
            'category': category,
            'bestsellers': Bestsellers.objects.all(),
        }

        return render(request, 'products/shop-detail.html', context=context)

    def post(self, request):
        comment = request.POST['comment']
        product = request.POST['product_c']
        comment_text = request.POST['comment_text']
        u_id = request.POST['u_id']
        print(product)

        a = Comments.objects.create(user_id=int(u_id), comment=comment_text, comment_title=comment)
        a.save()

        return redirect('thank')


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'products/cart.html')


class NotFound(View):
    def get(self, request):
        return render(request, 'products/404.html')

