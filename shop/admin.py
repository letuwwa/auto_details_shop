from django.contrib import admin
from .models import Category, Detail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title']


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['detail_title', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
