from django.db import models


class Menu(models.Model):
    name = models.CharField('Menu name', unique=True, max_length=200)
    slug = models.SlugField('Url', max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class MenuCategories(models.Model):
    category = models.CharField('Category', max_length=128)
    slug = models.SlugField('Url', max_length=120, unique=True, db_index=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Menu')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class MenuForCategory(models.Model):
    product = models.CharField('Product', max_length=128, unique=True)
    slug = models.SlugField('Url', max_length=120, unique=True, db_index=True)
    category = models.ForeignKey(MenuCategories, on_delete=models.CASCADE, verbose_name='Category')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
