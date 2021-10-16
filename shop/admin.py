from django.contrib import admin
from .models import Category, Detail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'slug']
    prepopulated_fields = {'slug': ('category_title',)}


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['detail_title', 'slug', 'category', 'price', 'available', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['available', 'category', 'created_at', 'updated_at']
    list_editable = ['price', 'category', 'available']
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug': ('detail_title',)}

