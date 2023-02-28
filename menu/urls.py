from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='menu'),
    path('<slug:menu_slug>/', MenuCategoriesView.as_view(), name='menu_cat'),
    path('<slug:menu_slug>/<slug:menu_cat_slug>/', MenuForCategoryView.as_view(), name='product'),
]
