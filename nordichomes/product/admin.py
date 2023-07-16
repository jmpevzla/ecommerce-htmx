from django.contrib import admin

from .models import Category, Product

class ProductInline(admin.TabularInline):
    model = Product
    raw_id_fields = ['category']
    fields = ['name', 'price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [ProductInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'description']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)