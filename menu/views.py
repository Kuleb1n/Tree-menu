from django.views.generic import TemplateView, ListView
from .models import *


class MainPageView(TemplateView):
    template_name = "base.html"


class MenuCategoriesView(ListView):
    model = MenuCategories
    template_name = "MenuCategories.html"
    context_object_name = 'Menu_Cat'

    def get_queryset(self):
        queryset = super(MenuCategoriesView, self).get_queryset()
        menu__slug = self.kwargs.get('menu_slug')
        return MenuCategories.objects.filter(
            menu__slug=menu__slug).select_related() if menu__slug else queryset.select_related()


class MenuForCategoryView(ListView):
    model = MenuForCategory
    template_name = "Products.html"
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(MenuForCategoryView, self).get_queryset()
        category__slug = self.kwargs.get('menu_cat_slug')
        return MenuForCategory.objects.filter(
            category__slug=category__slug).select_related() if category__slug else queryset.select_related()

    def get_context_data(self, *args, **kwargs):
        context = super(MenuForCategoryView, self).get_context_data()
        context['categories'] = MenuCategories.objects.filter(menu__slug=self.kwargs['menu_slug']).select_related()
        return context
