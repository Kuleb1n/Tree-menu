from django.contrib import admin
from .models import *


class CatAdminInline(admin.TabularInline):
    model = MenuCategories
    fields = ('category', 'slug')
    prepopulated_fields = {"slug": ("category",)}
    extra = 0


class ProductAdminInline(admin.TabularInline):
    model = MenuForCategory
    fields = ('product', 'slug')
    prepopulated_fields = {"slug": ("product",)}
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = (CatAdminInline,)


@admin.register(MenuCategories)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'slug')
    list_display_links = ('category',)
    search_fields = ('category',)
    prepopulated_fields = {"slug": ("category",)}
    inlines = (ProductAdminInline,)


@admin.register(MenuForCategory)
class MenuProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'slug')
    list_display_links = ('product',)
    search_fields = ('product',)
    prepopulated_fields = {"slug": ("product",)}
