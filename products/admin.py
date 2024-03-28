from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from products.models import Product, Category, Bestsellers, FeaturedItems


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'price', 'count']
    list_display_links = ['name', 'price', 'count']
    search_fields = ['name']


@admin.register(Bestsellers)
class BestsellersAdmin(ImportExportModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(FeaturedItems)
class FeaturedItemsAdmin(ImportExportModelAdmin):
    list_display = ['name', 'chegirma']
    list_display_links = ['name', 'chegirma']
    search_fields = ['name']

