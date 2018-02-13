from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/template_sites/top_cats.html')
def get_top_category_list():
    return {'cats': Category.objects.order_by('-likes')[:5]}

@register.inclusion_tag('rango/template_sites/latest_cats.html')
def get_latest_category_list():
    return {'cats': Category.objects.order_by('date')[:5]}
