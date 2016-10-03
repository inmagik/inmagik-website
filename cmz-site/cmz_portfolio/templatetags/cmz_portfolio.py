from django import template
from django.http import Http404

from ..models import PortfolioItem

register = template.Library()

def grouped(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

@register.simple_tag(takes_context=True)
def portfolio_list(context, group_size=0, num_items=None):
    page = context['request'].GET.get('page', 1);
    page = int(page)
    qset = PortfolioItem.objects.language().all()
    if num_items:
        qset = qset[(page-1)*num_items:num_items]

    if not group_size:
        return qset
    else:
        return grouped(qset, group_size)


@register.simple_tag(takes_context=True)
def portfolio_item(context, pk):
    try:
        item = PortfolioItem.objects.language().get(pk=pk)
    except PortfolioItem.DoesNotExist:
        raise Http404("Object not found!")
    return item
