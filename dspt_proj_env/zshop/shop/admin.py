from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name slug price available created updated'.split()
    list_filter = 'available created updated'.split()
    list_editable = 'price available'.split()
    prepopulated_fields = {'slug': ('name',)}

