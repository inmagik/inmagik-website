from django import template
from ..models import Tech

register = template.Library()

def grouped(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

@register.simple_tag(takes_context=True)
def tech_list(context, group_size=0):
    page = context['request'].GET.get('page', 1);
    page = int(page)
    #todo: add num pages, total items..
    #return Tech.objects.all()[(page-1)*num_items:num_items]
    qset = Tech.objects.language().all()
    if not group_size:
        return qset
    else:
        return grouped(qset, group_size)
