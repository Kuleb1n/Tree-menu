from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def draw_menu():
    return Menu.objects.all()


