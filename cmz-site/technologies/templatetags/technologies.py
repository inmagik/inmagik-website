from django import template
from ..models import Tech

register = template.Library()

@register.simple_tag(takes_context=True)
def tech_list(context, num_items=10):
    page = context['request'].GET.get('page', 1);
    page = int(page)
    #todo: add num pages, total items..
    #return Tech.objects.all()[(page-1)*num_items:num_items]
    return Tech.objects.language().all()[(page-1)*num_items:num_items]
